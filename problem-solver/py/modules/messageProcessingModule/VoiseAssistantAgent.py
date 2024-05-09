"""
Voice command agent code
"""
import logging
from sc_client.models import ScAddr, ScLinkContentType, ScTemplate
from sc_client.constants import sc_types
from sc_kpm.identifiers import CommonIdentifiers, QuestionStatus
from sc_client.client import template_search
from sc_kpm.utils.action_utils import execute_agent, call_agent, wait_agent
from sc_kpm import ScAgentClassic, ScModule, ScResult, ScServer
from sc_kpm.sc_sets import ScSet
from sc_client.client import template_generate , delete_elements
from sc_kpm.utils.action_utils import add_action_arguments, call_action, create_action, execute_action, wait_agent
from sc_kpm.utils import (
    create_link,
    get_link_content_data,
    check_edge, create_edge,
    delete_edges,
    get_element_by_role_relation,
    get_element_by_norole_relation,
    get_system_idtf,
    get_edge,
    get_edges
)
from sc_kpm.utils.action_utils import (
    create_action_answer,
    finish_action_with_status,
    get_action_arguments,
    get_element_by_role_relation
)
from sc_kpm import ScKeynodes
from sc_kpm.sc_sets import ScStructure

# --- agent libraries ---
import requests
from datetime import date, datetime
import speech_recognition
import pyttsx3
import re

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(message)s", datefmt="[%d-%b-%y %H:%M:%S]"
)
















class VoiseAssistantAgent(ScAgentClassic):
    def __init__(self):
        super().__init__("voice_action")
        self.inp_node_1 = ""
        self.inp_node_2 = ""
    



    def on_event(self, event_element: ScAddr, event_edge: ScAddr, action_element: ScAddr) -> ScResult:
        
        self.logger.info("Agent is up" )
        # --- set hardware ---
        self.create_edge_pattern = "Построить дугу из 'identifier' в 'identifier'"

        self.recognizer = speech_recognition.Recognizer()
        self.microphone = speech_recognition.Microphone()
        self.assistant()

        #Code example

        # node_1 = self.inp_node_1
        # node_2 = self.inp_node_2
        # node_1 = ScKeynodes[f"{node_1}"]
        # node_2 = ScKeynodes[f"{node_2}"]

        # self.logger.info(f"Get node {node_1} and node  {node_2}")
        
        # self.logger.info(" ")
        # self.logger.info("Connecting")
        # edge = create_edge(sc_types.EDGE_ACCESS_VAR_POS_PERM,node_1,node_2)

        # self.logger.info("Finish")
        return ScResult.OK

    def say(self,reply: str):
        engine = pyttsx3.init()
        engine.say(reply)
        engine.runAndWait()


   
        

        

    def record_and_recognize_audio(self,*args: tuple):
        """
        Запись и распознавание аудио
        """
        with self.microphone:
            recognized_data = ""

            # регулирование уровня окружающего шума
            self.recognizer.adjust_for_ambient_noise(self.microphone, duration=2)

            try:
                self.say("Начало")
                self.logger.info("Listening...")
                
                audio = self.recognizer.listen(self.microphone, 5, 5)

            except speech_recognition.WaitTimeoutError:
                self.logger.info("Can you check if your microphone is on, please?")
                return

            # использование online-распознавания через Google
            try:
                self.logger.info("Started recognition...")
                recognized_data = self.recognizer.recognize_google(audio, language="ru").lower()
                
            except speech_recognition.UnknownValueError:
                pass

            # в случае проблем с доступом в Интернет происходит выброс ошибки
            except speech_recognition.RequestError:
                self.logger.info("Check your Internet Connection, please")

            return recognized_data



    def assistant(self):
        time_prompt = ["сколько время", "сколько времени", "время"]
        date_prompt = ["какое сегодня число", "дата"]
        while True:
            voice_input = self.record_and_recognize_audio()
            self.logger.info(voice_input)
            self.recognition_filter(voice_input)
            self.say(voice_input)
            
            if voice_input in date_prompt:
                current_date = date.today()
                result = str(current_date.day) + " " + str(current_date.month) + " " + str(current_date.year)
                self.say(result)
            elif voice_input in time_prompt:
                current_time = datetime.now().time()
                result = str(current_time).split(":")[0] + " " + str(current_time).split(":")[1]
                self.say(result)
            elif voice_input == "стоп":  # окончание работы по команде "стоп"
                self.say("до свидания")
                break



    
    def get_nodes_create_identifiers(self,data,edge_flag):
        data_list = data.split(' ')
        identifier_1 = []
        identifier_2 = []
        end_words_list = ["до", "к", "в"]
        border = 0
        for end_word in end_words_list:
            if end_word in data_list:
                border = data_list.index(end_word)
                break
        

        if border:
            for word in data_list[:border]:
                if re.match(r'^[a-zA-Z]+$', word):
                    identifier_1.append(word)

            for word in data_list[border:]:
                if re.match(r'^[a-zA-Z]+$', word):
                    identifier_2.append(word)

            self.logger.info(identifier_1)
            self.logger.info(identifier_2)


            if edge_flag == True:
                self.build_edge(identifier_1,identifier_2)
            elif edge_flag == False:
                self.delete_edge(identifier_1,identifier_2)    
        else:

                 

            self.say("Invalid pattern")        

    


    def get_node_agent_create_identifiers(self,data):
        data_list = data.split(' ')
        identifier_1 = []

        for word in data_list[2:]:
            if re.match(r'^[a-zA-Z]+$', word):
                identifier_1.append(word)

        self.logger.info(identifier_1)   

        self.logger.info("Calling agent ...")

        self.call_agent()    

        


    def get_node_add_create_identifiers(self,data):
        data_list = data.split(' ')
        identifier_1 = []

        for word in data_list:
            if re.match(r'^[a-zA-Z]+$', word):
                identifier_1.append(word)

        self.logger.info(identifier_1)   

        self.logger.info("Calling node create function ...")

        self.call_node(identifier_1)   

    def get_node_delete_identifiers(self,data):
        data_list = data.split(' ')
        identifier_1 = []

        for word in data_list:
            if re.match(r'^[a-zA-Z]+$', word):
                identifier_1.append(word)

        self.logger.info(identifier_1)   

        self.logger.info("Calling node delete function ...")

        self.delete_node(identifier_1)    



    def get_template_identifiers(self,data):
        # data_list = data.split(' ')
        # identifier_1 = []

        # for word in data_list[2:]:
        #     if re.match(r'^[a-zA-Z]+$', word):
        #         identifier_1.append(word)

        # self.logger.info(identifier_1)   
        # self.logger.info("Calling template generator ...")
        self.call_template()      

     # --- Set of functions for ScAddr interaction


    def build_edge(self,identifier_1,identifier_2):
        node_1 = ScKeynodes[f"{identifier_1[0]}"]
        node_2 = ScKeynodes[f"{identifier_2[0]}"]

        self.logger.info(f"Get node {node_1} and node  {node_2}")
        
        self.logger.info(" ")
        self.logger.info("Connecting ...")
        edge = create_edge(sc_types.EDGE_ACCESS_VAR_POS_PERM,node_1,node_2)

        self.logger.info("Finish")


    def delete_edge(self,identifier_1,identifier_2):
        edge_list = []
        node_1 = ScKeynodes[f"{identifier_1[0]}"]
        node_2 = ScKeynodes[f"{identifier_2[0]}"]

        self.logger.info(f"Get node {node_1} and node  {node_2}")
        
        self.logger.info(" ")
        self.logger.info("Deleting ...")
        # status_code = delete_edges(node_1,node_2, sc_types.EDGE_ACCESS_VAR_POS_PERM)
        
        target_edges = get_edges(node_1,node_2, sc_types.UNKNOWN)

        self.logger.info(f"Addresses between nodes {target_edges}")
        
        status_code = delete_elements(*target_edges)
        self.logger.info(f"Delete status code {status_code}")
        self.logger.info("Finish")    




    def call_template(self,identifier_1):
        
        node_1 = ScKeynodes[f"{identifier_1[0]}"]



        msg = create_link(f"{identifier_1[0]} is test sc link,created by voice agent")
        msg = create_link(f"{identifier_1[0]} is test sc link for check agent")
        self.logger.info(f"{msg}")

        # relation_node = ScKeynodes["ground"]
        self.logger.info(f"Get node {node_1}")
        # self.logger.info(f"Ground address {relation_node}")

        template = ScTemplate()

        template.triple(
            node_1,
            sc_types.EDGE_ACCESS_VAR_POS_TEMP,
            (sc_types.NODE_VAR, '_var_node')
        )
        


        gen_params = {'_var_node': 'day'}
        gen_result = template_generate(template, gen_params)
        
        idtf_1 = get_system_idtf(gen_result[0])
        idtf_2 = get_system_idtf(gen_result[1])
        idtf_3 = get_system_idtf(gen_result[2])
        
        template_2 = ScTemplate()

        template_2.triple(
            msg,
            sc_types.EDGE_ACCESS_VAR_POS_TEMP,
            (sc_types.NODE_VAR, '_ex_node')
        )

        gen_2_params = {'_ex_node': f'{gen_result[0]}'}
        gen_2_result = template_generate(template_2, gen_2_params)
        self.logger.info(f"{len(gen_2_result)} is length of 2nd template")
        self.logger.info(f"{len(gen_result)} is length of 1st template")
        
        if len(gen_2_result) < 3:
            pass
        else:
            self.logger.info(f"{gen_2_result[0]} ")
            self.logger.info(f"{gen_2_result[1]} ")
            self.logger.info(f"{gen_2_result[2]} ")


        self.logger.info("Finish")


    def call_agent(self):
        # node_1 = ScKeynodes["year"]
        node_1 = create_link(1234567,ScLinkContentType.INT)

        self.logger.info(f"Get node {node_1}")
        self.logger.info(" ")
        self.logger.info("Call sub agent")
        
        # action_node = create_action(CommonIdentifiers.QUESTION, "check_node_action")

        # action_node = create_action(CommonIdentifiers.QUESTION, "question_search_full_semantic_neighborhood")
        action_node = create_action(CommonIdentifiers.QUESTION, "action_example_action")

        # self.logger.info(node_1)
        # node_1 = str(node_1)
        arguments = {node_1: False}
        add_action_arguments(action_node, arguments)
        call_action(action_node)
        wait_agent(3, action_node, ScKeynodes[QuestionStatus.QUESTION_FINISHED])
        # or
        is_successful = execute_action(action_node, wait_time=3)  # bool
        self.logger.info("Finish")



    def call_node(self,identifier_1):
        identifier_1 = str(identifier_1[0])
        self.logger.info(" ")
        self.logger.info("Call node create call")
        node_1 = ScKeynodes.resolve(f"{identifier_1}",sc_types.NODE_CONST_CLASS)
        self.logger.info(f"Create node {identifier_1}, address {node_1} ")
        self.logger.info("Finish")
    
    def delete_node(self,identifier_1):
        identifier_1 = str(identifier_1[0])
        self.logger.info(" ")
        self.logger.info("Call node delete call")
        node_1 = ScKeynodes.delete(f"{identifier_1}")
        self.logger.info(f"Delete node {identifier_1}, status {node_1}")
        self.logger.info("Finish")

    def recognition_filter(self,data: str):
        if "построить дугу" in data:
            self.get_nodes_create_identifiers(data,True)
        elif "удалить дугу" in data:
            self.get_nodes_create_identifiers(data,False) 

        elif "шаблон агента" in data:
            self.get_node_agent_create_identifiers(data)
        elif "шаблон генерации" in data:
            self.get_template_identifiers(data)

        elif "создать вершину" in data:
            self.get_node_add_create_identifiers(data)
        elif "удалить вершину" in data:
            self.get_node_delete_identifiers(data)
                  
