document.getElementById("output").src="https://c.tenor.com/nbB1q7b_TvcAAAAd/abstract.gif"

// handleSubmit je funkcia, ktora sa spusti ked sa bude mat odoslat nas formular
function handleSubmit(e) {
	e.preventDefault(); // zabranis vstavenemu odosielaniu v prehliadaci
	// this reprezentuje ten formular, ktory odosielame
	const ves = this.querySelector("textarea").value; // Nacitame text z textarea
	const width = document.querySelector("section:nth-child(2)").clientWidth; // Nacitame aktualnu sirku vystupneho okna
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
document.querySelector("form").addEventListener("submit", handleSubmit); // Nastavime formular, aby pri submit udalosti spustil nasu handleSubmit funkciu
function demo(e){
	e.preventDefault();
	document.querySelector("textarea").value ="VES v1.6 500 500 \nCLEAR #FF0000 \nFILL_TRIANGLE 200 100 400 300 300 300 #0000FF \nFILL_CIRCLE 200 100 50 #00FF00 \nFILL_RECT 400 100 150 200 #00FF00 \nCIRCLE 300 200 100 1 #FFFFFF \nTRIANGLE 50 100 200 300 150 200 1 #00FF00 \nRECT 200 100 300 100 1 #000000 \nLINE 0 0 599 499 1 #000000 ";
	document.getElementById("output").src="https://c.tenor.com/nbB1q7b_TvcAAAAd/abstract.gif";
} 
	
document.querySelector("form").addEventListener("submit", handleSubmit); 
document.querySelector("#demo").addEventListener("click", demo)

