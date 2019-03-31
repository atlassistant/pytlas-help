from pytlas import training, translations, intent, meta, Card
from pytlas.pam import get_loaded_skills

@training('fr')
def fr_training(): return """
%[help__get_skills]
  quelles sont tes ~[skills]
  qu'es-tu capable de faire
  que sais tu faire
  peux-tu m'aider
  dis moi de quoi tu es capable
  que peux-tu faire pour moi
  quels sont tes ~[skills]
  liste moi les ~[skills] installés

~[skills]
  skills
  compétences
  modules
  paquets
"""

@training('en')
def en_training(): return """
%[help__get_skills]
  what are your ~[skills]
  what are you able to do
  how can you help
  tell me what you are able to do
  what can you do for me
  show me your ~[skills]
  enumerates your installed ~[skills]

~[skills]
  skills
  modules
  packages
"""

@meta()
def help_meta(_): return {
  'name': _('help'),
  'description': _('List installed skills and provide some help'),
  'author': 'Julien LEICHER',
  'version': '1.0.0',
  'homepage': 'https://github.com/atlassistant/pytlas-help',
}

@translations('fr')
def fr_translations(): return {
  'Here what I know so far': 'Voilà ce que je sais faire pour le moment',
  'help': 'aide',
  'List installed skills and provide some help': "Liste les compétences installées et fourni de l'aide",
}

@intent('help__get_skills')
def on_get_skills(req):
  skills = get_loaded_skills(req.lang)
  cards = [Card(s.name, s.description, s.author, s.homepage) for s in skills]

  req.agent.answer(req._('Here what I know so far'), cards)

  return req.agent.done()