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


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(message)s", datefmt="[%d-%b-%y %H:%M:%S]"
)




class CheckNodeAgent(ScAgentClassic):
    def __init__(self):
        super().__init__("check_node_action")
        
    



    def on_event(self, event_element: ScAddr, event_edge: ScAddr, action_element: ScAddr) -> ScResult:
        
        self.logger.info("Check Agent is up" )
        # --- set hardware ---
        self.create_edge_pattern = "Построить дугу из 'identifier' в 'identifier'"
        self.call_agent()
        self.build_delete_edge(["some_class_name"],["some_class_name"])



        
    def check_nodes(self):
        node_check_list = ["day","note","delivery","manager","call","e-mail","filling","justification","year","temperature","engineering","knowledge","left","leaving","quantifier"]

        for node in node_check_list:

            try: 
                node_temp_addr = ScKeynodes[f"{node}"]

                self.logger.info(f"Get node {node},his address is {node_temp_addr} ")
            except:
                print(Exception)
        self.logger.info(" ")
        self.logger.info("Finish")
        

    def call_agent(self):
        node_1 = create_link(1234567,ScLinkContentType.INT)

        self.logger.info(f"Get node {node_1}")
        self.logger.info(" ")
        self.logger.info("Call sub agent")
        
        action_node = create_action(CommonIdentifiers.QUESTION, "action_example_action")
        arguments = {node_1: False}

        add_action_arguments(action_node, arguments)
        call_action(action_node)

        wait_agent(3, action_node, ScKeynodes[QuestionStatus.QUESTION_FINISHED])
        is_successful = execute_action(action_node, wait_time=3)  
       

        self.logger.info(" ")
        self.logger.info("Finish")


    def build_delete_edge(self,identifier_1,identifier_2):
        edge_list = []
        # node_1 = ScKeynodes[f"{identifier_1[0]}"]
        # node_2 = ScKeynodes[f"{identifier_2[0]}"]

        node_1 = ScKeynodes["day"]
        node_2 = ScKeynodes["note"]

        self.logger.info(f"Get node {node_1} and node  {node_2}")
        # --Создаем дугу
        edge = create_edge(sc_types.EDGE_ACCESS_VAR_POS_PERM,node_1,node_2)
        # --Удаляем дугу
        target_edges = get_edges(node_1,node_2, sc_types.UNKNOWN)
        target_edges_2 = get_edges(node_2,node_1, sc_types.UNKNOWN)

        self.logger.info(f"Addresses of all edges : {target_edges}")
        self.logger.info(f"Addresses of all edges : {target_edges_2}")
        status_code = delete_edges(node_1,node_2, sc_types.EDGE_ACCESS_VAR_POS_PERM)
        status_code_2 = delete_elements(*target_edges)
        status_code_3 = delete_elements(*target_edges_2)
        self.logger.info(" ")
        self.logger.info("Deleting ...")
        
        
        self.logger.info(f"Delete status code delete_edges : {status_code}")
        self.logger.info(f"Delete status code delete_elements : {status_code_2}")
        self.logger.info(f"Delete status code delete_elements : {status_code_3}")
        self.logger.info("Finish")   

        return ScResult.OK

    