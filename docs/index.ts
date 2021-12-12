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

    let elt = document.getElementById('doc');

    let tailleX = x.length;
    let tailleY = y.length;

    if (elt != null) {

        let newEltx = document.getElementById('xValeur');

        for (let i = x.length - 1; i >= 0; i--) {
            var tmp = document.createElement('div');
            //newElt.textContent = "toto";
            newEltx.appendChild(tmp);

            const name = "x" + (i + 1);
            createInput(name, name, "" + x[x.length - 1 - i], tmp);
        }

        let newElty = document.getElementById('yValeur');

        for (let i = y.length - 1; i >= 0; i--) {
            var tmp = document.createElement('div');
            //newElt.textContent = "toto";
            newElty.appendChild(tmp);

            const name = "y" + (i + 1);
            createInput(name, name, "" + y[y.length - 1 - i], tmp);
        }

        // valeurs intermediaires

        let eltValInterm = document.getElementById('valeursIntermediaires');

        for (let j = 0;j<y.length; j++) {

            var tmp = document.createElement('div');
            tmp.setAttribute("class", "d-flex justify-content-end")
            eltValInterm.appendChild(tmp);

            for (let i = x.length - 1; i >= 0; i--) {

                const name = "x" + (i + 1) + "*y" + (j + 1);
                createInput(name, name, "" + (x[x.length - i - 1] * y[y.length - j - 1]), tmp);

            }

            for (let k = 0; k < j; k++) {
                let tmp2 = document.createElement('div');
                tmp2.textContent = '.';
                tmp2.setAttribute("style", "width:50px;");
                tmp2.setAttribute("class", "text-center");
                tmp.appendChild(tmp2);
            }


        }

        // résultat

        let eltResultat = document.getElementById('resultat');

        for (let i = x.length - 1 + y.length - 1; i >= 0; i--) {
            const name = "z" + (i + 1);
            createInput(name, name, "", eltResultat);
        }

    }
}

let x = '';
let y = '';

// x="23";
// y="5";

//x = "100";
//y = "10";

x="123";
y="45";

construitCases(x, y);


