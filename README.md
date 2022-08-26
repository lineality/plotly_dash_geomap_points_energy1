#### plotly_dash_geomap_points_energy1

## To deploy in AWS EC2

Configuring EC2 is the usual chaos nightmare dumpster fire of AWS.



#### Instructions: In EC2 ssh/web-connect:
(for debian based linux use "apt" rather than "yum/dnf", etc.)

Steps:
```
$ sudo yum update -y

$ sudo yum install git -y

$ mkdir viz; dc viz

$ git clone https://github.com/lineality/plotly_dash_geomap_points_energy1.git

$ cd plotly_dash_geomap_points_energy1

$ python3 -m venv env; source env/bin/activate

(ENV)$ python3 -m pip install --upgrade pip

(ENV)$ pip install -r requirements.txt

(ENV)$ python3 app.py


```

# public ec2

view your live application by appending 8080 to your public IPv4Public IP address. 

