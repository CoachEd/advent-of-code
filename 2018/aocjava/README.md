# Updating to OpenJDK and OpenFX

## One-time setup for OpenJDK

* Download OpenJDK 11 (LTS) [link](https://adoptopenjdk.net/installation.html?variant=openjdk11&jvmVariant=hotspot)

    * OpenJDK 11 (LTS)
    * HotSpot
    * Download

* Extract downloaded file
* Folder is: `jdk-11.0.2+9`
* `sudo mv jdk-11.0.2+9 /Library/Java/JavaVirtualMachines`
* Make sure it is the only jdk in JavaVirtualMachines
* From Eclipse

    * Eclipse > Preferences...
    * Java > Installed JREs > Execution Environments
    * JavaSE-11
    * Check OpenJDK 11.0.2 [11.0.2][perfect match]
    * Apply and Close

## One time setup for JavaFX

* Download JavaFX 11 from: https://gluonhq.com/products/javafx/
* Unzip and extract openjfx-11.0.2_osx-x64_bin-sdk.zip
* Copy the javafx-sdk-11.0.2 folder to a comman area: cp javafx-sdk-11.0.2 /Users/ertorres
* Start Eclipse

    * Eclipse > Preferences... > Java > Build Path > User Libraries > New...
    * User library name: JavaFX11
    * Highlight JavaFX11 , Add External JARs...
    * Navigate to javafx-sdk-11.0.2/lib and select *.jar *.zip 
    * Apply and Close

## Project specific

* Right-click project > Properties > Java Build Path > Libraries
* Highlight Modulepath > Add Library... > JRE System Library > Next > Workspace default JRE (OpenJDK 11.0.2)
* Finish
* Highlight Classpath
* Add Library...
* User Library
* Check JavaFX11
* Add library...
* User library
* Check JaaFX11-jmods
* Finish
* Apply and Close
* Create a Java Project: _JRE: Use default JRE (currently 'OpenJDK 11.0.2 [11.0.2]')
* Don't create module info file

## Program specific

* Right-click project > Run As > Run Configurations...
* Highlight your program
* Click the (x)= Arguments tab
* In VM arguments, type these two parameters, including your correct path: `--module-path /Users/ertorres/javafx-sdk-11.0.2/lib --add-modules javafx.controls,javafx.fxml`
* *Uncheck* _Use the -XstartOnFirstThread argument when launching with SWT_
* Click the JRE tab
* Select Alternate JRE: OpenJDK 11.0.2
* Apply
* Run
