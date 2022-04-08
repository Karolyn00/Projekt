let example = document.getElementById("example")
let ves = document.getElementById("ves")

example.addEventListener("change", ()=>{
	let fr = new FileReader();
	fr.readAsText(example.files[0]);
	fr.onload = function(){
		ves.innerHTML = fr.result;};})

function stlacenie() {
	document.getElementById("#ves").innerText = "
	VES v1.6 500 500
	CLEAR #F1B48C
	FILL_RECT 225 -10 50 699 #000000
	FILL_TRIANGLE 100 100.1 400 100 250 360 #FFFFFF
	TIANGLE 100 400 250 140 400 400 3 #FFFFFF
	CIRCLE 250 250 75 1 #000000
	LINE 275 320 225 180 1 #000000
	LINE 275 180 225 320 1 #000000
	LINE 180 275 320 225 1 #000000
	LINE 180 225 320 275 1 #000000
	FILL_RECT 225 225 50 50 #F1B48C
	LINE 250 215 285 250 3 #F1B48C
	LINE 285 250 250 285 3 #F1B48C
	LINE 250 285 215 250 3 #F1B48C
	LINE 215 250 250 215 3 #F1B48C
	FILL_CIRCLE 250 250 10 #000000
	CIRCLE 250 250 20 3 #FFFFFF
	FILL_CIRCLE 225 180 15 #000000
	FILL_CIRCLE 275 180 15 #000000
	FILL_CIRCLE 225 320 15 #000000
	FILL_CIRCLE 275 320 15 #000000
	FILL_CIRCLE 180 225 15 #000000
	FILL_CIRCLE 320 225 15 #000000
	FILL_CIRCLE 180 275 15 #000000
	FILL_CIRCLE 320 275 15 #000000
	FILL_CIRCLE 225 180 14 #F1B48C
	FILL_CIRCLE 275 180 14 #F1B48C
	FILL_CIRCLE 225 320 14 #F1B48C
	FILL_CIRCLE 275 320 14 #F1B48C
	FILL_CIRCLE 180 225 14 #F1B48C
	FILL_CIRCLE 320 225 14 #F1B48C
	FILL_CIRCLE 180 275 14 #F1B48C
	FILL_CIRCLE 320 275 14 #F1B48C
	FILL_CIRCLE 400 250 55 #000000
	FILL_CIRCLE 435 250 55 #F1B48C
	FILL_CIRCLE 100 250 55 #000000
	FILL_CIRCLE 65 250 55 #F1B48C
	RECT 10 10 480 480 2 #000000";}
	

// handleSubmit je funkcia, ktor� sa spust� ke� sa bude ma� odosla� n� formul�r

function handleSubmit(e) {

	e.preventDefault(); // zabr�ni� vstaven�mu odosielaniu v prehliada�i


	// this reprezentuje ten formular, ktory odosielame

	const ves = this.querySelector("textarea").value; // Na��tame text z textarea

	const width = document.querySelector("section:nth-child(2)").clientWidth; // Na��tame aktu�lnu ��rku v�stupn�ho okna


	const formular = new URLSearchParams(); // Vytvor�me �trukt�ru, ktor� bude reprezentova� formul�r

	formular.append('ves', ves); // Prid�me tam na�e hodnoty

	formular.append('width', width);


	const url = this.action; // Nacitame povodnu URL zadanu vo formulari

	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari

	fetch(url, {method: method, body: formular}) // Urob�me HTTP po�iadavku na n� server POST /render a formularom v tele po�iadavky
 
		.then((res) => res.blob()) // Dostali sme bin�rne d�ta (blob)

		.then((image) => {

			document.querySelector("#output").src = URL.createObjectURL(image); // Nastav�me src na�eho <img> na na��tan� obr�zok

		})
}
document.querySelector("form").addEventListener("submit", handleSubmit); // Nastav�me formul�r, aby pri submit udalosti spustil na�u handleSubmit funkciu


