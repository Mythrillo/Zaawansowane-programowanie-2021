# Zaawansowane Programowanie - Projekt

Aby móc odpalić projekt należy wykonać następujące kroki. 
1. Projekt napisany w Python 3.10.0
2. `pip install -r requirements.txt`
3. Pobrać plik: http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet50_coco_2018_01_28.tar.gz i wypakować z niego plik `frozen_inference_graph.pb` do folderu `models. Spowodowane jest to wielkością pliku większą niż 100MB.
4. `python app.py`
5. Wejść w przeglądarce na http://127.0.0.1:5000/