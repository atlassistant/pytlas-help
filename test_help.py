from sure import expect
from pytlas.testing import create_skill_agent
from pytlas.skill import Meta
from unittest.mock import patch
import os

class TestGetHelp:

  def test_it_should_returns_loaded_skills_correctly(self):
    skills = [
      Meta(name='alpha', description='An alpha skill', author='Julien LEICHER'),
      Meta(name='bravo', description='A bravo skill', author='John Doe'),
    ]

    # Here we need to patch the method before importing the skill
    with patch('pytlas.pam.get_loaded_skills', return_value=skills):
      agent = create_skill_agent(os.path.dirname(__file__), lang='en')
      agent.parse('how can you help')

      call = agent.model.on_answer.get_call()

      expect(call.text).to.equal('Here what I know so far')
      expect(call.cards).to.have.length_of(2)

      expect(call.cards[0].header).to.equal('alpha')
      expect(call.cards[0].text).to.equal('An alpha skill')
      expect(call.cards[0].subhead).to.equal('Julien LEICHER')

      expect(call.cards[1].header).to.equal('bravo')
      expect(call.cards[1].text).to.equal('A bravo skill')
      expect(call.cards[1].subhead).to.equal('John Doe')


