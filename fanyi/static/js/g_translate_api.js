google.load("language", "1");
    
    function submitChange() {
        var text = document.getElementById('text').value;
        //var dest = document.getElementById('dst').value;
        google.language.translate(text, "se", "en", translateResult);
        return false;
    }
    
    function translateResult(result) {
      var resultBody = document.getElementById("translation_en");
      if (result.translation) {
        var str = result.translation.replace('>', '&gt;').replace('<', '&lt;');
        resultBody.innerHTML = str;
      } else {
        resultBody.innerHTML = '<span style="color:red">Error Translating</span>';
      }
      
      var text = document.getElementById('text').value;
      google.language.translate(text, "se", "zh-CN", translateResultZh);
      
    }
    
    function translateFromTyda(result){
        
        var src = document.getElementById('text').value;
        
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("GET","tyda?src="+src.toLowerCase(),true);
        xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        
        xmlhttp.onreadystatechange=function() {
            if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var en_words_list = xmlhttp.responseText;
                var tyda_en_words_div = document.getElementById("tyda_en_words");
                if(en_words_list != ""){
                    tyda_en_words_div.innerHTML = en_words_list;
                
                    google.language.translate(en_words_list, "se", "zh-CN", translateResultZh2);
                }else{
                    tyda_en_words_div.innerHTML = '<span style="color:red">Error Translating From tyda</span>';
                }
                
            }
        }
        xmlhttp.send(null);
        
    }
    
    function translateResultZh2(result){
        var zh_words_div = document.getElementById("zh_words");
        if(result.translation) {
            var str = result.translation.replace('>', '&gt;').replace('<', '&lt;');
            zh_words_div.innerHTML = str;
            
            //save the tyda translation result
            var en_translate = document.getElementById("tyda_en_words").innerHTML;
            var zh_translate = document.getElementById("zh_words").innerHTML;
            var src = document.getElementById('text').value;
        
            xmlhttp=new XMLHttpRequest();
            xmlhttp.open("POST","addTyda",true);
            xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
            xmlhttp.send("src="+src.toLowerCase()+"&translation_en="+en_translate.toLowerCase()+"&translation_zh="+zh_translate);
        }else {
            zh_words_div.innerHTML = '<span style="color:red">Error Translating</span>';
        }
        
        
    }
    
    function translateResultZh(result){
        var resultBody = document.getElementById("translation_zh");
        if(result.translation) {
            var str = result.translation.replace('>', '&gt;').replace('<', '&lt;');
            resultBody.innerHTML = str;
        }else {
            resultBody.innerHTML = '<span style="color:red">Error Translating</span>';
        }
        
        var en_translate = document.getElementById("translation_en").innerHTML;
        var zh_translate = document.getElementById("translation_zh").innerHTML;
        var src = document.getElementById('text').value;
        
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("POST","add",true);
        xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        xmlhttp.send("src="+src.toLowerCase()+"&translation_en="+en_translate.toLowerCase()+"&translation_zh="+zh_translate);
        
        http://tyda.se/search?form=1&w=omfattning
        var tydaDiv = document.getElementById("tyda");
        //tydaDiv.innerHTML = '<a href="http://tyda.se/search?form=1&w='+src+'" target="_blank">tyda.se</a>';
        tydaDiv.innerHTML = '<input id="clearButton" class="button" type="button" onClick="javascript:translateFromTyda();" value="Tyda"/>';
        
        //clear the tyda translation result
        document.getElementById("tyda_en_words").innerHTML="";
        document.getElementById("zh_words").innerHTML="";
    }
    
    function clearInput(){
        document.getElementById('text').value = "";
    }