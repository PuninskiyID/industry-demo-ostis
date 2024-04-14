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
from sc_client.client import template_generate
from sc_kpm.utils.action_utils import add_action_arguments, call_action, create_action, execute_action, wait_agent
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

        node_check_list = ["day","note","delivery","manager","call","e-mail","filling","justification","year","temperature","engineering","knowledge","left","leaving","quantifier"]

        for node in node_check_list:

            try: 
                node_temp_addr = ScKeynodes[f"{node}"]

                self.logger.info(f"Get node {node},his address is {node_temp_addr} ")
            except:
                print(Exception)

        self.logger.info(" ")
        self.logger.info("Finish")
        return ScResult.OK

    