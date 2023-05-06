sh ./cluster/create_cluster.sh && \
sh ./resources/load_images.sh && \
sh ./resources/apply_deployments.sh && \
sh ./resources/apply_service.sh && \
sh ./resources/create_ingress_controller.sh && \
sh  ./resources/apply_ingress.sh