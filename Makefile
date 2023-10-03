.phony: connect-hadoop
connect-hadoop:
	- gcloud compute ssh cluster-wikihunt-m

.phony: to-hadoop
to-hadoop:
	- ssh -i ~/.ssh/wikihunt-laptop reqhiem@34.139.213.107
