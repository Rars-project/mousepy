# Hand Gesture Tracking and Recognition Based Human-Computer Interaction System
## INTRUDUCTION 
>A mouse is a data input device that helps to point and to interact with whatever that's being pointed. In a hardware device like mouse we can still face latency related issues and in rare cases it affects the reliability of the system. Because the mouse will have a durability time within which is functional and after its durability time we've to vary the mouse.
Different techniques are being proposed for gaining necessary information/data for the recognition of gestures. Some models work with special devices like data glove devices and color caps to develop a piece of complex information about gestures provided by the user/human. Similarly, the virtual mouse that we'll discuss in this project is formed from OpenCV and PyAutoGUI.</BR>
</BR>
>OpenCV is a python library for computer vision that is employed for capturing images from a webcam and PyAutoGUI is a python library that's used for specifying keyboard and mouse operations.</BR></BR>
>Technologies like Artificial Intelligence and Machine Learning have become booming technologies that help us easily to work and provide commands to systems with no human interactions. So here the model is additionally a neighborhood-color hose technology which may help us work with our systems with ease. 

## Hardware Requirements 
> * Webcam : 640x480 pixels or above
> * Hard disk : 500GB
> * Processor : Dual core or greater
> * Ram : 8GB or more 
> * Also it needs Python and all the Requirements packeges from Requriment.txt needed


## Implementation of the system
 * >The Front-end is designed using PyQt5 QtDesigner tool. PyQt5 is a cross-platform
GUI toolkit, a set of python bindings for Qt v5. The GUI mainly consists of two
modes i.e., Gesture based interaction and virtual mouse. In Gesture based interaction
mode we are using jester model which is trained under RT3D_16F and twenty-BN
jester dataset. It is necessary to adapt continuously, identifying when a gesture was
performed and only then assign a label to the prediction. For that we used a window
of the 16 most recent frames obtained, which updates itself with each new frame
acquired.</br></br>
 * >In virtual mouse mode we have created an AI based Mouse controller. This is
implemented using media pipe library, this library is a free and open-source
framework under apache2.0 which is fully extensible and customizable and works
across several platforms like android, iOS, desktop or cloud, web and Iot.</br>
We are detecting the hand landmarks and then it is tracked and mouse operations is
performed based on these hand landmarks. Mouse operations can be performed by
using PyAutoGUI library and hand landmarks can be found out by using findHands()
and findPosition() methods of HandTracking Module. Then we are finding the tip of
the all the fingers and checks which fingers are up. If only the index finger is up then
moving mode is activated.</br> Similarly, if both index and middle fingers are up then left
click operation is performed, only when the distance between these two-tip id’s is
less than 40. PyAutoGUI.leftClick() method is used to perform left click operation of
the mouse. 


>### Gesture Informations are available at Our  Website 
>* [ Mousepy ](https://mousepy.netlify.app/web/index.html)
>* [Github -Source code ](https://github.com/Rars-project/mousepy)

> ## For more info contact us

| Name            | Email                           | 
| :-------------  |:-------------                   | 
| Rithesh         | ritheshrai5@gmail.com           | 
| Rohan J billava | rjbillava24091999@gmail.com     |   
| Adarsha k       | adarshakanthabailu@gmail.com    |   
| Sebastian       | sebastianthomas075@gmail.com    |   


