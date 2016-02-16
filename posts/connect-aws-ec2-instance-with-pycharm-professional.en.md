<!-- 
.. title: Connect AWS EC2 Instance with PyCharm Professional
.. slug: connect-aws-ec2-instance-with-pycharm-professional
.. date: 2016-02-16 17:49:43 UTC+09:00
.. type: text
-->

- **Download [Pycharm Professional](https://www.jetbrains.com/pycharm/download/index.html)** and Install it.
	![Pycharm Professional Download Page](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/01_pycharm_download_webpage.png)

- Launch PyCharm - **Check out from Github**
	![Select "Check out from Version Control - Github"](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/02_pycharm_main_for_checkout_github.png)
	
- Login - **Clone Repository**
	![Select Projects](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/03_pycharm_clone_project.png)

- Open it
	![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/04_pycharm_open_project.png)
	
- **Tools - Deployments - Configuration**
	![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/05_pycharm_tools_deployment_configuration.png)

- **Add SFTP Server**
	![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/06_pycharm_tools_deployment_configuration_add_aws_sftp.png)
	- SFTP Host : **Elastic IP** or Public DNS
	- Root Path : **Autodetect**
	- User Name : `ubuntu` (default for AWS Ubuntu)
	- Auth Type : **Key Pair**
	- Private Key File
	- Web server root URL : `http://HOST:PORT`
		![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/07_pycharm_tools_deployment_configuration_add_aws_sftp_details.png)
	- Set **Deployment path**
		![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/08_pycharm_tools_deployment_configuration_add_aws_sftp_details_mapping.png)

- Check **Automatic Upload**
	![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/09_pycharm_tools_deployment_auto_upload.png)
	
- **Preferences - Project - Project Interpreter - Add Remote**
	![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/10_preferences_project_interpreter.png)

- Use **Deployment Configuration**
	- Set **your interpreter path** (**NEED TO BE CHANGE HERE!**)
	![](https://minhoryang.github.io/_/connect-aws-ec2-instance-with-pycharm-professional.en.md/11_preferences_project_interpreter_deployment.png)