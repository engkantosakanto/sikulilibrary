 #!/bin/bash

export sikulix_jar="sikuli-script.jar"
export robot_framework_jar="robotframework-2.8.7.jar"

java -cp "$robot_framework_jar:$sikulix_jar" -Dpython.path="$sikulix_jar/Lib" org.robotframework.RobotFramework --pythonpath=sikulilibrary.sikuli --outputdir=results --loglevel=TRACE $*
