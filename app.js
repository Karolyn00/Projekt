let example = document.getElementById("example")
let ves = document.getElementById("ves")

example.addEventListener("change", ()=>{
	let fr = new FileReader();
	fr.readAsText(example.files[0]);
	fr.onload = function(){
		ves.innerHTML = fr.result;};})


	

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


