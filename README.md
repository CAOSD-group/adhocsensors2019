Steps to replicate the experiments for measuring the energy consumption of the energy consuming concerns.

# EXPERIMENTATION FOR DEVICE 1 (Raspberry Pi).

## Requirements:
	* Raspberry Pi 3 Model B (https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
		* Raspbian 8 (Jessie) system
	* WattsUp? Pro Meter (https://www.powermeterstore.com/p1206/watts_up_pro.php)
		* WattsUpUSB desktop application
	* Provided Python scripts.
	
## Set up:
	1. Connect power suply of the Raspberry Pi to the WattsUp? Pro Meter.
	2. Connect power suply of the WattsUp? Pro Meter to the wall plug (the Raspberry PI will turn on and launch the OS).
	3. Connect the WattsUp? Pro Meter with an desktop PC using the USB port.
	4. Launch the WattsUpUSB desktop application.
	5. Install drivers of WattsUp? Pro Meter following the application wizard (only the first time).
	6. Calibrate the WattsUp? Pro Meter following the application wizard (only the first time).
	7. Configure parameters to log -> Meter Setting -> Logged Items -> Select only Watts.
	
	
	
## Perform the measurements (the following actions are performed in the Desktop).
	1. Before each experiments:
		1.1. Clear the meter data. In the WattsUp application -> Meter Setting -> Memory tab -> Clear Meter Data.
		1.2. Wait until Raspberry Pi stabilizes in the iddle status of power ~[1.7-1.9] W.

	2. WattsUp? Pro Meter is continuosly logging power consumption.
	3. Between each run, leave a temporal gap between each execution to allow RaspberryPi stabilizes in the iddle status of power.
	4. After the desired number of runs of each experiment:
		4.1. Clic on Request Data on the WattsUp application.
		4.2. Check the results are correct. Clic on Graph tabs. Different runs should be identifiable in the energy consumption graph.
		4.2. Save the results. File -> Save Table As...

	5. Run the Python script "wattsup-meter-v5.py" with the result file as argument and a standard deviation expected for the iddle status power of the device (e.g., 0.1 W).
	(see -help for different options).
	The script generates a file with a summary of the energy information and shows that information in the terminal.
	
	
## Experiments for the desired functionality with the desired configuration (energy consuming concern). 
	(The following actions are performed in the Raspberry Pi).

	1. Experiments for simulating the monitorization.
		1.1. Generate the simulated files of parameters, images or text to be used in the following experiments (Step 3).
			To do that, execute the appropriate Python script attached. 
			* generate_random_image.py
			* generate_random_parameters.py
			* generate_random_text.py
				
			See -help to launch the script with different configurations.	
		
	2. Experiments for compression:
			Example 1. For compression using the DEFLATE algorithm, in a terminal execute the following command:
				time gzip -6 file
				where 6 is the compression ratio and file is the file of parameters, images or text, generated in Step 1 (simulating the monitorization).
			Example 2. For compression using the Burrow-Wheeler algorithm, in a terminal execute the following command:
				time bzip2 -6 file
				where 6 is the compression ratio and file is the file of parameters, images or text, generated in Step 1 (simulating the monitorization).
			Example 3. For compression using the LZMA2 algorithm, in a terminal execute the following command:
				time xz -6 file
				where 6 is the compression ratio and file is the file of parameters, images or text, generated in Step 1 (simulating the monitorization).
	3. Experiments for communication:
			Example 4. For sending a file throught the network, in a terminal execute the following command:
				time spc file your_username@remotehost.edu:/some/remote/directory
				where file is the file of parameters, images or text (compressed or not) to be sent, and the second parameters is the server (remote host).
	4. Experiments for archiving:
			Example 5. For archiving a file in an archive, in a terminal execute the following command:
				time tar cvf file.tar file
				where file is the file to be archive within the file.tar archive.

				

# DEVICE 2 (Geo-location sensor).

## Requirements:
	* A mobile phone with GPS sensor and Snapdragon CPU.
		* Android system.
	* Trepn Profile application installed on the phone.
	* Provided Android application.
	* Provided Python scripts.
	
## Set up:
	1. Connect the phone to the Desktop using USB and the developer debug option active.
	2. Install the provided Android applications in the phone throught Android Studio. 
	3. Configure TrepnProfile in the mobile. Preferences -> check to log only battery power -> save file as "hadas_preferences.pref"
	4. Connect the phone to the adb of Android using WiFi connection:
		4.1. In a Windows terminal execute:
			adb tcpip 55555
			adb connect IP_of_the_mobile:5555
	5. Disconnect the phone USB.
	6. Run the script-GPS.bat in Windows. Android application will be run in the mobile. Activate GPS and get the GPS location in the app button.
		After 60 seconds the script will finish and generate the file with the energy consumption values.
		