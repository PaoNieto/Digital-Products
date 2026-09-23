# -*- coding: utf-8 -*-
"""Avisa que paginas del PDF se pasan de alto (o sea: donde se cortaria el texto).

  python revisar.py

Mide cada .pagina adentro del navegador y compara el alto real del contenido con
el alto util de la hoja. Es mas rapido y mas seguro que abrir el PDF y mirar de a
una pagina. Correrlo cada vez que se toca el contenido.
"""
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
NAV = next((r for r in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            if os.path.exists(r)), None)
if not NAV:
    sys.exit("No encontre Chrome ni Edge.")

SONDA = """<script>window.addEventListener('load',function(){
  var r=[];
  document.querySelectorAll('.pagina').forEach(function(p,i){
    if(p.classList.contains('tapa-p'))return;
    var cs=getComputedStyle(p);
    /* offsetTop de un hijo ya viene medido desde el borde de arriba de .pagina */
    var tope=p.clientHeight-parseFloat(cs.paddingBottom);
    var alto=0;
    p.childNodes.forEach(function(n){
      if(n.nodeType!==1)return;
      var s=getComputedStyle(n);
      if(s.position==='absolute')return;
      alto=Math.max(alto, n.offsetTop+n.offsetHeight+parseFloat(s.marginBottom));
    });
    var t=(p.querySelector('h1')||p.querySelector('.seccion')||{}).textContent||('#'+i);
    if(alto>tope-4) r.push('SE PASA '+Math.round(alto-tope)+'px | hoja '+(i+1)+' | '+t.trim().slice(0,44));
  });
  document.title='RESULTADO::'+(r.length?r.join(' ;; '):'todo entra');
});</script>"""


def revisar(archivo):
    src = open(os.path.join(AQUI, archivo), encoding="utf-8").read()
    tmp = os.path.join(AQUI, "_sonda.html")
    open(tmp, "w", encoding="utf-8").write(src.replace("</body>", SONDA + "</body>"))
    salida = subprocess.run(
        [NAV, "--headless", "--disable-gpu", "--virtual-time-budget=5000", "--dump-dom",
         "file:///" + tmp.replace("\\", "/")],
        capture_output=True, timeout=180).stdout.decode("utf-8", "ignore")
    os.remove(tmp)
    m = re.search(r"RESULTADO::(.*?)</title>", salida, re.S)
    print("\n== " + archivo)
    for linea in (m.group(1) if m else "no pude medir").split(" ;; "):
        print("   " + linea.strip())


if __name__ == "__main__":
    revisar("plana-todo-el-dia.html")
