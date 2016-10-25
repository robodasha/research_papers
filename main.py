"""
Project main
"""

import sys
import logging

from crossref_resolver.logutils import setup_logging

__author__ = 'robodasha'
__email__ = 'damirah@live.com'


def exit_app():
    """
    Exit app
    :return: None
    """
    print('Exiting')
    exit()


def menu():
    """
    Just print menu
    :return: None
    """
    print('\nPossible actions:')
    print('=================')
    for key in sorted(menu_actions):
        print('{0}: {1}'.format(key, menu_actions[key].__name__))
    print('Please select option(s)')
    # enable selecting multiple actions which will be run in a sequence
    actions = [i.lower() for i in list(sys.stdin.readline().strip())]
    exec_action(actions)
    return


def exec_action(actions):
    """
    Execute selected action
    :param actions:
    :return: None
    """
    if not actions:
        menu_actions['x']()
    else:
        print('\nSelected the following options: \n{0}'.format(
            [(key, menu_actions[key].__name__)
             if key in menu_actions
             else (key, 'invalid action')
             for key in actions]))
        for action in actions:
            if action in menu_actions:
                menu_actions[action]()
            else:
                pass
    menu()
    return


menu_actions = {
    'x': exit_app,
    'm': menu,
}


if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Application started')
    try:
        menu()
    except Exception as e:
        logger.exception(e, exc_info=True)

