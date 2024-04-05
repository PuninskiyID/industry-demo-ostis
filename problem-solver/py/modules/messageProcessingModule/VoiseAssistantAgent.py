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

import requests


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(message)s", datefmt="[%d-%b-%y %H:%M:%S]"
)
















class VoiseAssistantAgent(ScAgentClassic):
    def __init__(self):
        super().__init__("voice_test_action")
        



    def on_event(self, event_element: ScAddr, event_edge: ScAddr, action_element: ScAddr) -> ScResult:
        
        result = self.run(action_element)
        is_successful = result == ScResult.OK

    def run(self,action_element):
        self.logger.info('*' * 20 + 'Voise assistant is up' + '*' * 20 )    
        # Get sc-link with raw text    

        coagulator = ScKeynodes["сoagulator"]   

        print(coagulator) 
        # base_voice_node = get_action_arguments(action_element)
        
        # if not base_voice_node:
        #     self.logger.error('Error: could not start voice  assistant process')
        #     return ScResult.ERROR_INVALID_PARAMS
        
        #Get language of raw text sc-link
        # language_template = ScTemplate()
        # language_template.triple(
        #     sc_types.NODE_CLASS,
        #     sc_types.EDGE_ACCESS_VAR_POS_PERM,
        #     base_voice_node
        # )

        # search_result = template_search(language_template)
        # print(search_result)


        return ScResult.OK
    #     if len(search_result) != 1:
    #         self.logger.error('Error: You have passed no language or too many arguments.')
    #         return ScResult.ERROR_INVALID_PARAMS
    #     language_node = search_result[0][0]
    #     language = get_system_idtf(language_node)
    #     if not language in cf.AVAILABLE_LANGUAGES:
    #         self.logger.error(f'Error: you have not passed available language as argument. You passed: {language}')
    #         return ScResult.ERROR_INVALID_PARAMS
        
    #     # Get raw text string
    #     raw_text = get_link_content_data(base_voice_node)        
    #     if not isinstance(raw_text, str):
    #         self.logger.error(f'Error: your raw text link must be string type, but text of yours is {type(raw_text)}')
    #         return ScResult.ERROR_INVALID_TYPE

    #     # Trying to get clean text        
    #     try:
    #         clean_text = self._get_clean_text(raw_text, language)            
    #     except Exception as err:
    #         self.logger.error(f'Error: {err}.\nThis error is on local LLM\'s side.')
    #         return ScResult.ERROR
        
    #     # Check text for emptiness. If processed text is empty, that means that model does not work
    #     if clean_text is None or clean_text == '':
    #         self.logger.error(f'Error: local LLM does not work. Try to change it or use other processing method.')
    #         return ScResult.ERROR

    #     # Creating answer and finishing agent work
    #     answer_link = create_link(clean_text, ScLinkContentType.STRING)        
    #     create_action_answer(action_element, answer_link)
    #     self.logger.info('Successfully processed the text using local LLM.')
    #     finish_action_with_status(action_element, True)
    #     return ScResult.OK

    # def run(self, action_node: ScAddr) -> ScResult:
    #     self.logger.info("ExampleAgent started")

    #     link = create_link(
    #         "smth", ScLinkContentType.STRING, link_type=sc_types.LINK_CONST)
 
    #     create_action_answer(action_node, link)

    #     return ScResult.OK
