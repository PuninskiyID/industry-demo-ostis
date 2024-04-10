"""
This code creates some test agent and registers until the user stops the process.
For this we wait for SIGINT.
"""
import logging
from sc_client.models import ScAddr, ScLinkContentType, ScTemplate
from sc_client.constants import sc_types
from sc_client.client import template_search

from sc_kpm import ScAgentClassic, ScModule, ScResult, ScServer
from sc_kpm.sc_sets import ScSet
from sc_kpm.utils import (
    create_link,
    get_link_content_data,
    check_edge, create_edge,
    delete_edges,
    get_element_by_role_relation,
    get_element_by_norole_relation,
    get_system_idtf,
    get_edge
)
from sc_kpm.utils.action_utils import (
    create_action_answer,
    finish_action_with_status,
    get_action_arguments,
    get_element_by_role_relation
)
from sc_kpm import ScKeynodes


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




        node_1 = self.inp_node_1
        node_2 = self.inp_node_2
        node_1 = ScKeynodes[f"{node_1}"]
        node_2 = ScKeynodes[f"{node_2}"]

        self.logger.info(f"Get node {node_1} and node  {node_2}")
        
        self.logger.info(" ")
        self.logger.info("Connecting")
        edge = create_edge(sc_types.EDGE_ACCESS_CONST_POS_PERM,node_1,node_2)

        self.logger.info("Finish")
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
            self.recognition_filter(voice_input)
            self.say(voice_input)
            self.logger.info(voice_input)
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

    def get_nodes_identifiers(self,data):
        data_list = data.split(' ')
        identifier_1 = []
        identifier_2 = []
        end_words_list = ["до", "к", "в"]
        for end_word in end_words_list:
            if end_word in data_list:
                border = data_list.index(end_word)
                break

        for word in data_list[:border]:
            if re.match(r'^[a-zA-Z]+$', word):
                identifier_1.append(word)

        for word in data_list[border:]:
            if re.match(r'^[a-zA-Z]+$', word):
                identifier_2.append(word)

        self.logger.info(identifier_1)
        self.logger.info(identifier_2)


        node_1 = ScKeynodes[f"{identifier_1[0]}"]
        node_2 = ScKeynodes[f"{identifier_2[0]}"]

        self.logger.info(f"Get node {node_1} and node  {node_2}")
        
        self.logger.info(" ")
        self.logger.info("Connecting")
        edge = create_edge(sc_types.EDGE_ACCESS_CONST_POS_PERM,node_1,node_2)

        self.logger.info("Finish")

       


    def recognition_filter(self,data: str):
        if "построить дугу" in data:
            self.get_nodes_identifiers(data)