from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import Django
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Celery
from diagrams.generic.device import Mobile
from diagrams.onprem.monitoring import Grafana

graph_attr = {"fontsize": "20", "bgcolor": "white", "pad": "0.3"}

with Diagram("EcoRecicla AQP - Vista de despliegue", filename="docs/architecture/diagramas/img/despliegue", show=False,
             direction="LR", graph_attr=graph_attr, outformat="png") as diag:
    vecinos = Users("Vecinos y\nMunicipalidad")
    recicladores = Mobile("PWA Reciclador\n(Celular 3G)")
    
    with Cluster("Servidor Privado Virtual (VPS)"):
        proxy = Nginx("Nginx\n(Reverse Proxy / HTTPS)")
        with Cluster("Monolito Modular"):
            app = Django("Django App\n(5 Módulos)")
            worker = Celery("Celery Worker\n(Reportes asíncronos)")
            cache = Redis("Redis\n(Caché y Broker)")
        db = PostgreSQL("PostgreSQL\n(Base de datos)")
        mon = Grafana("Monitoreo\n(Prometheus / Logs)")
        
    vecinos >> proxy
    recicladores >> proxy
    proxy >> app
    app >> db
    app >> Edge(label="encola tareas") >> cache >> worker
    worker >> Edge(label="reportes batch", style="dashed")
    app >> Edge(style="dotted") >> mon
