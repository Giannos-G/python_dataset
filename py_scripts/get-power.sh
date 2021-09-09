#!/bin/bash


rm module-power-input.txt
rm GPU-power.txt
rm CPU-power.txt
#rm main-carrier-board-power-input.txt
#rm main-carrier-board-5V-supply.txt
#rm main-carrier-board-3.3V-supply.txt
#rm carrier-board-3.3V-sleep-supply.txt
#rm main-carrier-board-1.8V-supply.txt
#rm 3.3V-supply-for-M.2-key-E-connector.txt
rm prof_time.txt


while true; do
	start=$(($(date +%s%N)/1000000))

  cat /sys/bus/i2c/drivers/ina3221x/7-0040/iio\:device0/in_power0_input >> module-power-input.txt
  cat /sys/bus/i2c/drivers/ina3221x/7-0040/iio\:device0/in_power1_input >> GPU-power.txt
  cat /sys/bus/i2c/drivers/ina3221x/7-0040/iio\:device0/in_power2_input >> CPU-power.txt

#  cat /sys/bus/platform/devices/7000c400.i2c/i2c-1/1-0042/iio_device/in_power0_input >> main-carrier-board-power-input.txt
#  cat /sys/bus/platform/devices/7000c400.i2c/i2c-1/1-0042/iio_device/in_power1_input >> main-carrier-board-5V-supply.txt
#  cat /sys/bus/platform/devices/7000c400.i2c/i2c-1/1-0042/iio_device/in_power2_input >> main-carrier-board-3.3V-supply.txt

#  cat /sys/bus/platform/devices/7000c400.i2c/i2c-1/1-0043/iio_device/in_power0_input >> carrier-board-3.3V-sleep-supply.txt
#  cat /sys/bus/platform/devices/7000c400.i2c/i2c-1/1-0043/iio_device/in_power1_input >> main-carrier-board-1.8V-supply.txt
#  cat /sys/bus/platform/devices/7000c400.i2c/i2c-1/1-0043/iio_device/in_power2_input >> 3.3V-supply-for-M.2-key-E-connector.txt

	end=$(($(date +%s%N)/1000000))
	echo $((end-start)) >> prof_time.txt

 #sleep 0.001s
done
