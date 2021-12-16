

function search(){
  var text = document.getElementById("keyword-input").value
  var info;
  if (text != null){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/search_resume", true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    var data = {
      'text' : text,
    }
    xhr.send(JSON.stringify(data));
    console.log(text);

    xhr.onreadystatechange = (e) => {
      info = xhr.response;
      console.log(info);
      nodes = [];
      model = document.getElementById("result");
      child = model.children;
      console.log(child);
      // This needs fixed and its done
      model.childNodes.item("HERE").childNodes.item("username").innerText = info[0]["fname"] + " " +  info[0]["lname"];

      }
      // for (var i = 1; i < info.length; i++){
      //   node = model.cloneNode();
      //   node.id = "i";
      //   child = node.children;
      //   for (var i = 0; i < child.length; i++){
      //     if (child[i].id == "username"){
      //       child[i].innerText = info[i]['user']['fname'] + " " +  info[i]['user']['lname'];
      //       break;
      //     }
      // }
      //   nodes.push(node);
      // }
    //}
    }

}
window.onload = function(){
  document.getElementById("database-div").addEventListener("click", search);
}
