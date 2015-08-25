@echo off

set sikulix_jar=sikuli-script.jar
set robot_framework_jar=robotframework-2.9.jar

java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=sikulilibrary.sikuli ^
     --outputdir=results ^
     --loglevel=TRACE ^
     %*
