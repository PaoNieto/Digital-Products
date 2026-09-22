# Herramientas del espía: cuándo y con qué cuidado

Orden por defecto: **Biblioteca de Meta a mano primero** (gratis). Las herramientas
conectadas se usan solo cuando la Biblioteca se queda corta, y ninguna se usa para
lanzar, clonar ni pausar anuncios (eso es de Bilbito, después de 10 ventas).

Regla de plata (la mejor costumbre que se vio en herramientas del rubro): **antes de
cualquier llamada que gaste cuota o créditos, decir cuánto cuesta y esperar el OK de
Paolo.** "Esto usa 1 de tus 3 altas del día" antes, no después.

## AdWhispr (conector de Claude)

Sirve para ver de golpe todos los anuncios de un anunciante ordenados por antigüedad,
que es justo la señal de ¿ya se paga?. Aparece con dos nombres de conector (AdWhispr
Ads y adWhispr); las herramientas de lectura son las mismas.

| Herramienta | Para qué | Costo o cuidado |
|---|---|---|
| `get_my_brand` | ver qué marca tiene guardada la cuenta | gratis. **Llamarla primero** |
| `search_brands` | buscar un anunciante ya seguido, por nombre | lectura |
| `get_brand_ads` con `sortBy: longevity` | anuncios activos del anunciante, los más viejos primero | lectura. Por defecto trae solo activos: dejarlo así |
| `get_brand_stats` | resumen del anunciante (cantidad de anuncios, formatos) | lectura |
| `search_ads` | buscar por concepto dentro de un anunciante (pide su id) | lectura |
| `find_competitors` con `niche` | anunciantes verificados como activos en un nicho | usa cuota. **Siempre pasar `niche`** con la frase del comprador, para no depender de la marca guardada |
| `add_brand` | empezar a seguir un anunciante nuevo | tope diario (3 por día en el plan gratis) y borrar no devuelve el cupo: uno por vez, solo si Paolo lo pidió |
| `research_tiktok_ads` | anuncios de TikTok de un anunciante (modo ads) o videos orgánicos de un creador (modo organic) | modo ads: solo Europa y sin gasto; modo organic sirve para cualquier cuenta pública |

Prohibido para El Gato:

- `save_my_brand` y `clear_my_brand`: la marca guardada puede ser la de Vendí. Pisarla
  mezcla los dos negocios. Si `get_my_brand` devuelve Vendí, se trabaja con `niche` y
  con anunciantes por nombre, sin tocar lo guardado.
- Todo lo que empieza con `launch_`, `clone_`, `pause_`, `resume_`, `update_budget`,
  `connect_ad_account`: es pauta, es de Bilbito.

Ojo con sus números: puntajes de rendimiento, ingresos estimados o gasto estimado son
**estimaciones de la herramienta**, no datos de Meta. Van como "no verificado". La señal
confiable es la misma de la Biblioteca: días corriendo y creativos activos.

## Apify (conector de Claude)

Sirve solo si hay que bajar cientos de anuncios a una planilla. Para 1 a 3 compradores
candidatos, no hace falta. Puede aparecer desconectado: si falla, se sigue con la
Biblioteca a mano y se le avisa a Paolo que el conector no conectó.

1. `search-actors` con "facebook ad library" → elegir por uso y reseñas. Los nombres de
   los actores no están verificados acá: se leen en el resultado, no se inventan.
2. `fetch-actor-details` → leer qué pide de entrada y **cuánto cobra**.
3. Decirle a Paolo el costo estimado y esperar el OK.
4. `call-actor` → `get-dataset-items` para leer el resultado.
5. Lo que sale se filtra con los mismos umbrales (3+ días, 7+ creativos) y va a
   `digimones/mercado.md` con fecha y fuente "Apify, actor <nombre>".

## Lo que ninguna herramienta cambia

- El veredicto sale de días corriendo y creativos activos, no del puntaje de una app.- Nada de Vendí entra ni sale por estas herramientas.
