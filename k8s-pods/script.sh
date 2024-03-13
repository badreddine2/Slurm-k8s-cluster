service_info=$(kubectl get svc slurmc-service)

ip_address=$(echo "$service_info" | awk 'NR>1 {print $3}')

echo "IP Address: $ip_address"

sudo sed -i "s/ControlMachine=.*/ControlMachine=$ip_address/" /etc/slurm/slurm.conf
sudo sed -i "s/ControlAddr=.*/ControlAddr=$ip_address/" /etc/slurm/slurm.conf
