var words = document.querySelectorAll('table.prettytable a'),
    txt = '';

for (let i = 0; words[i] != undefined; i++)
    txt = txt + words[i].innerHTML + '\n';

var res = document.createElement('textarea');
res.style.position = 'fixed';
res.style.top = '0';
res.style.bottom = '0';
res.style.zIndex = '4';
res.style.width = '100px';
res.style.height = '400px';
res.innerHTML = txt;

document.body.appendChild(res);
