# Advent of Code

Solutions for the Advent of Code coding competition: [link](https://adventofcode.com/)

All solutions use `Python 3.x`

## Java

See this to install OpenJFX and OpenJDK: https://github.com/CoachEd/openjfx-example
Use this Eclipse for Java Developers:
https://www.eclipse.org/downloads/packages/release/2019-09/r/eclipse-ide-java-developers
New Java project, but don't create a module
Windows > Preferences > Java > Installed JREs > add jdk-11.0.5.10-hotspot 
Windows > Preferences > Java > Compiler > Select compiler compliance level 11
Right-click project > Properties > Java Build Path

  * Modulepath - add all JavaFX SDK JAR files
  * Add JRE System Library (jdk-11.0.5.10-hotspot)
  * Classpath - add JavaFX library runtime

Program-specific run configuration, add VM argument: --module-path $OPENFX_SDK/lib/ --add-modules=javafx.controls







