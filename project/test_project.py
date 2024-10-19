import pytest
from unittest.mock import patch  
import project

def test_generate_key():
    gen = project.generate_key('aymen',2)
    assert next(gen) == project.to_b_64ecode('a')
    assert next(gen) == project.to_b_64ecode('y')
def test_encrypt():
    data = {'a':'text1',
            'b':'text2',}
    en_data = project.encrypt(data,project.generate_key('aymen',2))
    des = project.decrypt(en_data,project.generate_key('aymen',2))
    assert des['a'] == data['a']
    assert des['b'] == data['b']
def test_decrypt():
    data = {'a':'text1',
        'b':'text2'}
    assert project.decrypt(project.encrypt(data,project.generate_key('aymen',2)),project.generate_key('aymen',2))['a'] == data['a']
    assert project.decrypt(project.encrypt(data,project.generate_key('aymen',2)),project.generate_key('aymen',2))['b'] == data['b']
