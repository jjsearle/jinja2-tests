import os
from template import Template


def test_template_obj():
    t = Template(template_file="test1.conf.j2",
                 output_directory=".")
    assert t.template_file == "test1.conf.j2"
    assert t.output_directory == "."
    assert t.output_filename == "test1.conf"


def test_template_render_create_outfile():
    if os.path.exists("test1.conf"):
        os.remove("test1.conf")
    t = Template(template_file="test1.conf.j2",
                 output_directory=".")
    t.render()
    assert os.path.isfile("test1.conf")
    os.remove("test1.conf")


def test_template_render_defaults():
    if os.path.exists("test1.conf"):
        os.remove("test1.conf")
    t = Template(template_file="test1.conf.j2",
                 output_directory=".")
    t.render()
    f = open("test1.conf", "r")
    contents = f.read()
    f.close()
    os.remove("test1.conf")
    assert contents == "param1=1"


def test_template_render_env():
    if os.path.exists("test1.conf"):
        os.remove("test1.conf")
    os.environ["PARAM1"] = "WORKS"
    t = Template(template_file="test1.conf.j2",
                 output_directory=".")
    t.render()
    f = open("test1.conf", "r")
    contents = f.read()
    f.close()
    os.remove("test1.conf")
    assert contents == "param1=WORKS"
