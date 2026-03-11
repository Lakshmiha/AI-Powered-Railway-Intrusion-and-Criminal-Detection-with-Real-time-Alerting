# !pip
# install
# roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="L4WW1dnA50JsyezYlpWv")
project = rf.workspace("amaya-w9w1d").project("railway-tfabb-awnfe")
version = project.version(1)
dataset = version.download("yolov12")
