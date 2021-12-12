// function greeter(person) {
//   return "Hello, " + person;
// }
function createInput(name, placeholder, value, parent) {
    var tmp2 = document.createElement('input');
    tmp2.setAttribute("type", "text");
    tmp2.setAttribute("name", name);
    tmp2.setAttribute("placeholder", placeholder);
    tmp2.setAttribute("value", value);
    tmp2.setAttribute("class", "case");
    parent.appendChild(tmp2);
}
// let user = "Jane User";
//document.body.textContent = greeter(user);
function construitCases(x, y) {
    var elt = document.getElementById('doc');
    var tailleX = x.length;
    var tailleY = y.length;
    if (elt != null) {
        var newEltx = document.getElementById('xValeur');
        for (var i = x.length - 1; i >= 0; i--) {
            var tmp = document.createElement('div');
            //newElt.textContent = "toto";
            newEltx.appendChild(tmp);
            var name_1 = "x" + (i + 1);
            createInput(name_1, name_1, "" + x[x.length - 1 - i], tmp);
        }
        var newElty = document.getElementById('yValeur');
        for (var i = y.length - 1; i >= 0; i--) {
            var tmp = document.createElement('div');
            //newElt.textContent = "toto";
            newElty.appendChild(tmp);
            var name_2 = "y" + (i + 1);
            createInput(name_2, name_2, "" + y[y.length - 1 - i], tmp);
        }
        // valeurs intermediaires
        var eltValInterm = document.getElementById('valeursIntermediaires');
        for (var j = 0; j < y.length; j++) {
            var tmp = document.createElement('div');
            tmp.setAttribute("class", "d-flex justify-content-end");
            eltValInterm.appendChild(tmp);
            for (var i = x.length - 1; i >= 0; i--) {
                var name_3 = "x" + (i + 1) + "*y" + (j + 1);
                createInput(name_3, name_3, "" + (x[x.length - i - 1] * y[y.length - j - 1]), tmp);
            }
            for (var k = 0; k < j; k++) {
                var tmp2 = document.createElement('div');
                tmp2.textContent = '.';
                tmp2.setAttribute("style", "width:50px;");
                tmp2.setAttribute("class", "text-center");
                tmp.appendChild(tmp2);
            }
        }
        // résultat
        var eltResultat = document.getElementById('resultat');
        for (var i = x.length - 1 + y.length - 1; i >= 0; i--) {
            var name_4 = "z" + (i + 1);
            createInput(name_4, name_4, "", eltResultat);
        }
    }
}
var x = '';
var y = '';
// x="23";
// y="5";
//x = "100";
//y = "10";
x = "123";
y = "45";
construitCases(x, y);
