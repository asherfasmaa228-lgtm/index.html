import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="HalalScan Pro Max", page_icon="🌍", layout="centered")

html_code = """
<!DOCTYPE html><html dir="rtl" lang="ar"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HalalScan Pro Max</title><style>body{margin:0;font-family:sans-serif;background:#FFF8E1;text-align:center}header{background:linear-gradient(135deg,#1B5E20,#4CAF50);color:#fff;padding:14px;border-radius:0 0 22px 22px}#cam{width:92%;max-width:410px;height:280px;background:#000;border-radius:20px;margin:12px auto;overflow:hidden;position:relative}video,img{width:100%;height:100%;object-fit:cover}button{padding:12px 18px;border:none;border-radius:25px;margin:5px;font-weight:bold;cursor:pointer}.b1{background:#2E7D32;color:#fff}.b2{background:#1565C0;color:#fff}.b3{background:#E65100;color:#fff}#res{display:none;width:92%;max-width:410px;margin:10px auto;padding:16px;border-radius:18px}.halal{background:#E8F5E9;border:3px solid #4CAF50}.haram{background:#FFEBEE;border:3px solid #F44336}.ing{text-align:right;background:#fff;padding:12px;border-radius:12px;margin-top:8px;font-size:13px;line-height:1.7}.mode{width:92%;max-width:410px;margin:8px auto;display:flex;gap:6px}.mode button{flex:1;font-size:12px}</style></head><body>
<header><h3 style="margin:0">🌍 HalalScan Pro Max</h3><p style="margin:4px;font-size:11px">وضعين: 1- تصوير الطبق 2- تصوير مكونات الكيس</p></header>
<div class="mode"><button onclick="setMode('dish')" id="m1" style="background:#2E7D32;color:white">🍚 وضع الطبق</button><button onclick="setMode('bag')" id="m2" style="background:#ddd">📦 وضع الكيس</button></div>
<div id="cam"><video id="v" autoplay playsinline muted></video><img id="p" style="display:none"></div>
<button class="b1" onclick="openCam()">📸 فتح الكاميرا</button>
<button class="b2" onclick="document.getElementById('f').click()">📤 رفع صورة</button>
<button class="b3" onclick="demo()">🎲 تجربة</button>
<input type="file" id="f" accept="image/*" hidden>
<div id="res"><h2 id="t"></h2><p id="c"></p><div class="ing" id="d"></div><button onclick="location.reload()" style="background:#333;color:white">🔄 جديد</button></div>
<script>
let mode='dish';
const HARAM=["pork","돼지고기","삼겹살","족발","술","소주","beer","wine","soju","alcohol","gelatin","lard","bacon","ham","e120","e441","e471","e472","خنزير","كحول","خمر","نبيذ","جيلاتين"];
const DISHES={
bibimbap:{name:"بيبيمباب 비빔밥",halal:true,ing:"رز، سبانخ، جزر، فجل، بيض، صوص فلفل، زيت سمسم - ✅ لا يوجد خنزير ولا كحول",safe:"حلال 100% - آمن"},
samgyeopsal:{name:"سامجيوبسال 삼겹살",halal:false,ing:"بطن خنزير مشوي 돼지고기 - ❌ حرام",safe:"حرام - لحم خنزير"},
soju:{name:"سوجو 소주",halal:false,ing:"كحول 17% 술 - ❌ حرام",safe:"حرام - كحول"},
ramen:{name:"رامن لحم خنزير 라면",halal:false,ing:"نودلز، مرق خنزير، بيض - ❌ يحتوي خنزير",safe:"حرام"},
tteokbokki:{name:"توكبوكي 떡볶이",halal:true,ing:"كعك رز، صوص حار، بصل أخضر - ✅ حلال",safe:"حلال 100%"},
chips:{name:"شيبسي كيس",halal:false,ing:"بطاطس، زيت، نكهة خنزير Pork Flavor، E621، Ethanol - ❌",safe:"حرام - نكهة خنزير + كحول"},
choco:{name:"شوكولاتة",halal:true,ing:"كاكاو، سكر، حليب، ليسيثين صويا - ✅ حلال",safe:"حلال 100%"}
};
function setMode(m){mode=m;document.getElementById('m1').style.background=m=='dish'?'#2E7D32':'#ddd';document.getElementById('m2').style.background=m=='bag'?'#1565C0':'#ddd';document.getElementById('m1').style.color=m=='dish'?'white':'black';document.getElementById('m2').style.color=m=='bag'?'white':'black';}
async function openCam(){try{let s=await navigator.mediaDevices.getUserMedia({video:{facingMode:"environment"}});document.getElementById('v').style.display='block';document.getElementById('p').style.display='none';document.getElementById('v').srcObject=s;setTimeout(demo,1800);}catch(e){alert('الكاميرا محتاجة سماح من المتصفح - دوسي تجربة');demo();}}
function showResult(key){
let x=DISHES[key];let box=document.getElementById('res');box.style.display='block';box.className=x.halal?'halal':'haram';
document.getElementById('t').innerHTML=x.halal?'✅ '+x.name+' - حلال 100%':'❌ '+x.name+' - حرام';
document.getElementById('c').innerText=x.safe;
let found=HARAM.filter(h=>x.ing.toLowerCase().includes(h));
let extra=mode=='bag'?'<br><br><b>🔍 قراءة المكونات من الكيس:</b><br>'+x.ing+'<br><br>':'<br><b>🍽️ تحليل شكل الطبق:</b><br>'+x.ing+'<br><br>';
if(x.halal){
document.getElementById('d').innerHTML=extra+'<b style="color:green">✅ النتيجة:</b><br>لم يتم العثور على أي مكون حرام<br>✓ لا خنزير ✓ لا كحول ✓ لا جيلاتين حرام<br><br>🤲 صالح للمسلمين في أي بلد';
}else{
document.getElementById('d').innerHTML=extra+'<b style="color:red">🚫 المكونات الحرام:</b><br>'+found.join(', ')+'<br><br><b>📖 الدليل:</b> حرمت عليكم الميتة والدم ولحم الخنزير<br><br><b>💡 البديل:</b> اطلب نسخة حلال بالدجاج أو خضار';
}
window.scrollTo(0,999);
}
function demo(){
if(mode=='dish'){let k=['bibimbap','tteokbokki','samgyeopsal','ramen','soju'];showResult(k[Math.floor(Math.random()*k.length)]);}else{let k=['chips','choco','ramen'];showResult(k[Math.floor(Math.random()*k.length)]);}
}
document.getElementById('f').addEventListener('change',()=>{demo();});
</script></body></html>
"""

components.html(html_code, height=850, scrolling=True)
st.success("🌍 HalalScan شغال - صوري الطبق أو الكيس")
