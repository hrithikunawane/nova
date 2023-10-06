@ECHO OFF
:: tug_intel.bat: Responsible for performing machine driven system reconnaissance.
:: Segment alpha: User intel
ECHO ---------------------------------------- USER ----------------------------------------
WHOAMI
ECHO ---------------------------------------- /USER ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- USER [EXPANDED] ----------------------------------------
NET USER HRITHIK
ECHO ---------------------------------------- /USER [EXPANDED] ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- USERS ----------------------------------------
NET USER
ECHO ---------------------------------------- /USERS ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- HOSTNAME ----------------------------------------
HOSTNAME
ECHO ---------------------------------------- /HOSTNAME ----------------------------------------
ECHO,
ECHO,
:: Segment beta: System intel
ECHO ---------------------------------------- SYSTEM ----------------------------------------
SYSTEMINFO
ECHO ---------------------------------------- /SYSTEM ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- SERVICES ----------------------------------------
TASKLIST /SVC
ECHO ---------------------------------------- /SERVICES ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- SCHEDULED TASKS ----------------------------------------
SCHTASKS /QUERY /FO LIST /V
ECHO ---------------------------------------- /SCHEDULED TASKS ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- RW ENABLED ----------------------------------------
ACCESSCHK.EXE -UWS "EVERYONE" "C:\Program Files"
ECHO ---------------------------------------- /RW ENABLED ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- DRIVER ----------------------------------------
DRIVERQUERY
ECHO ---------------------------------------- /DRIVER ----------------------------------------
ECHO,
ECHO,
:: Segment gamma: Network intel
ECHO ---------------------------------------- NETWORK ----------------------------------------
IPCONFIG /ALL
ECHO ---------------------------------------- /NETWORK ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- ROUTING TABLE ----------------------------------------
ROUTE PRINT
ECHO ---------------------------------------- /ROUTING TABLE ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- ACTIVE CONNECTIONS ----------------------------------------
NETSTAT -ANO
ECHO ---------------------------------------- /ACTIVE CONNECTIONS ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- FIREWALL STATUS ----------------------------------------
NETSH ADVFIREWALL SHOW CURRENTPROFILE
ECHO ---------------------------------------- /FIREWALL STATUS ----------------------------------------
ECHO,
ECHO,
ECHO ---------------------------------------- FIREWALL RULES ----------------------------------------
NETSH ADVFIREWALL FIREWALL SHOW RULE NAME=ALL
ECHO ---------------------------------------- /FIREWALL RULES ----------------------------------------
ECHO,
ECHO,
CALL tug_intel.bat > Intel_Scratch.txt