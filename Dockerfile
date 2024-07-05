FROM odoo:17

# If you have to install from pip and using Odoo >= 11.0
USER root
ENV PATH="/var/lib/odoo/.local/bin:${PATH}"
RUN pip3 install paramiko
