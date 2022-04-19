document.getElementById("output").src="https://c.tenor.com/nbB1q7b_TvcAAAAd/abstract.gif"

// handleSubmit je funkcia, ktora sa spusti ked sa bude mat odoslat nas formular
function handleSubmit(e) {
	e.preventDefault(); // zabranis vstavenemu odosielaniu v prehliadaci
	// this reprezentuje ten formular, ktory odosielame
	const ves = this.querySelector("textarea").value; // Nacitame text z textarea
	const width = document.querySelector("div:nth-child(2)").clientWidth; // Nacitame aktualnu sirku vystupneho okna
	const formular = new URLSearchParams(); // Vytvorime strukturu, ktoru bude reprezentovat formular
	formular.append('ves', ves); // Pridame tam nase hodnoty
	formular.append('width', width);
	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // Nacitame povodnu metodu zadanu vo formulari
	fetch(url, {method: method, body: formular}) // Urobime HTTP poziadavku na na server POST /render a formularom v tele poziadavky
		.then((res) => res.blob()) // Dostali sme binarne data (blob)
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image); // Nastavime src naseho <img> na nacitany obrazok
		})
}

function clear(e) {
	e.preventDefault();
	document.querySelector("textarea").value = "VES v1.6 500 500";
	document.getElementById("output").src="https://c.tenor.com/nbB1q7b_TvcAAAAd/abstract.gif";}

document.querySelector("form").addEventListener("submit", handleSubmit); // Nastavime formular, aby pri submit udalosti spustil nasu handleSubmit funkciu
document.querySelector("#clear").addEventListener("click", clear)
