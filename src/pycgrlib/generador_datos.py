import random as r
import json

# Lista de nombres masculinos
nombres_masculinos = ['Alejandro', 'Alberto', 'Andrés', 'Manuel', 'Guillermo', 'Alexander', 'José Damian', 'Damian', 'Daniel', 'José Francisco', 'Francisco', 'Jeffrey', 'David', 'Kevin', 'Bryan', 'Johan', 'Miguel', 'Alex', 'Berny', 'Bob', 'Claudio', 'Carlos', 'Eduardo', 'Esteban', 'Fabricio', 'Fernando', 'Gabelo', 'Gustavo', 'Jose Manuel', 'Jose David',
                      'Ignacio', 'Iselmo', 'Hugo', 'Halberth', 'Kenneth', 'Kendal', 'Lando', 'Larry', 'Mario', 'Mariano', 'Nelson', 'Napoleon', 'Osbaldo', 'Oliver', 'Paolo', 'Pablo', 'Quinto', 'Querubin', 'Rodrigo', 'René', 'Ricardo', 'Santiago', 'Sebastián', 'Tiago', 'Teodoro', 'Ulises', 'Ubaldo', 'Valerio', 'Víctor', 'Walter', 'William', 'Xavier', 'Yoel', 'Zacarías']
# Lista de nombres femeninos
nombres_femeninos = ['Lilliana', 'Aurora', 'Amelia', 'Belén', 'Bianca', 'Carolina', 'Carmen', 'Daniela', 'Diana', 'Elena', 'Ericka', 'Fernanda', 'Fátima', 'Graciela', 'Gabriela', 'Harley', 'Hellen', 'Inés', 'Isabel', 'Julia', 'Jazmín', 'Karina', 'Karen', 'Keren', 'Lia', 'Lusiana', 'Marisol', 'Marisa', 'Marina', 'Melissa', 'Mia', 'María', 'Miriam', 'Natalia', 'Nadia', 'Noemi', 'Norma',
                     'Ofelia', 'Olivia', 'Olga', 'Paz', 'Pia', 'Paola', 'Paloma', 'Rosa', 'Rosario', 'Rafaela', 'Rebeca', 'Rocio', 'Salomé', 'Sabrina', 'Silvia', 'Susana', 'Samantha', 'Tatiana', 'Tamara', 'Tracy', 'Tania', 'Ursula', 'Uriana', 'Única', 'Viviana', 'Valeria', 'Verónica', 'Valery', 'Wanda', 'Windy', 'Ximena', 'Yazmin', 'Yuridia', 'Yolanda', 'Zaleth', 'Zadith', 'Zara', 'Zaira']
# Lista de apellidos
apellidos = ['Madriz', 'González', 'Rojas', 'Díaz', 'Muñoz', 'Zamora', 'Pérez', 'Martinez', 'Hernandez', 'Torres', 'Flores', 'Reyes', 'Silva', 'López', 'Espinoza', 'Gutierrez', 'Castro', 'Piza', 'Fernández', 'Ramirez', 'Rivera', 'García', 'Miranda', 'Campos', 'Órtiz', 'Salazar', 'Guzmán', 'Navarro', 'Vidal', 'Romero', 'Lagos', 'Medina', 'Alvarado', 'Moreno', 'Bustamante', 'Ortega', 'Mendoza', 'Zamora', 'Zuñiga', 'Arrieta', 'Arias', 'Jiménez', 'Mora', 'Vargas', 'Castro',
             'Sánchez', 'Morales', 'Cruz', 'Ramos', 'Álvarez', 'Castillo', 'Villavicencio', 'De la Cruz', 'Del Monte', 'Smith', 'Parks', 'Loria', 'Tévez', 'Monge', 'Pereira', 'Zamorano', 'Sáenz', 'Lemaitre', 'Gómez', 'Quirós', 'Solís', 'Robles', 'Mora', 'Solano', 'Alfaro', 'Rueda', 'Santisteban', 'Moreno', 'Cañas', 'Monteverde', 'Calle', 'Palma', 'Lobo', 'Galarga', 'Pozo', 'Sepúlveda', 'Díaz', 'Calvo', 'Rosal', 'Chan', 'Ali', 'Wang', 'Li', 'Wu', 'Xiao', 'Chang', 'Mao', 'Qiang', 'Jian']

# Lista de lugares
lugares = ["del Puente", "de la Cantina", "de la Iglesia", "de la Pulperia", "del Parque", "de la Bomba", "de la Escuela",
           "del Colegio", "del Hotel", "del Restaurante", "del Cementerio", "del Estadio", "de la Plaza", "del Mercado", "del Edificio"]

# Lista de nombres de lugares
nombre_lugares = ["Del Norte", "Los Liguistas", "Saprissa", "Los Anonos", "Los Monazos", "El rey del norte", "El guayabo", "Central", "Del Norte", "Cristiana", "Palo de Mango", "El Rey", "Santos de los ultimos Dias",
                  "La Amistad", "Del Sur", "Mono Azul", "Guachiperrin", "Los Manazos", "de Montaña", "McDonalds", "Perpetuo Socorro", "Los Guayabos", "Las Perlas", "El ocaso", "Las ánimas perdidas"]

# Objeto JSON con las provincias, cantones y distritos de CR.
ubicaciones = '''{
	"title": "Costa Rica",
	"provincias": [
		{
			"title": "San José",
			"cantones": [
				{
					"title": "San José",
					"distritos": [
						{"title": "Carmen"},
						{"title": "Merced"},
						{"title": "Hospital"},
						{"title": "Catedral"},
						{"title": "Zapote"},
						{"title": "San Fco. de Dos Ríos"},
						{"title": "Uruca"},
						{"title": "Mata Redonda"},
						{"title": "Pavas"},
						{"title": "Hatillo"},
						{"title": "San Sebastián"}
					]
				},
				{
					"title": "Escazú",
					"distritos": [
						{"title": "Escazú"},
						{"title": "San Antonio"},
						{"title": "San Rafael"}
					]
				},
				{
					"title": "Desamparados",
					"distritos": [
						{"title": "Desamparados"},
						{"title": "San Miguel"},
						{"title": "San Juan de Dios"},
						{"title": "San Rafael Arriba"},
						{"title": "San Antonio"},
						{"title": "Frailes"},
						{"title": "Patarrá"},
						{"title": "San Cristóbal"},
						{"title": "Rosario"},
						{"title": "Damas"},
						{"title": "San Rafael Abajo"},
						{"title": "Gravilias"},
						{"title": "Los Guido"}
					]
				},
				{
					"title": "Puriscal",
					"distritos": [
						{"title": "Santiago"},
						{"title": "Mercedes Sur"},
						{"title": "Barbacoas"},
						{"title": "Grifo Alto"},
						{"title": "San Rafael"},
						{"title": "Candelaria"},
						{"title": "Desamparaditos"},
						{"title": "San Antonio"},
						{"title": "Chires"}
					]
				},
				{
					"title": "Tarrazú",
					"distritos": [
						{"title": "San Marcos"},
						{"title": "San Lorenzo"},
						{"title": "San Carlos"}
					]
				},
				{
					"title": "Aserrí",
					"distritos": [
						{"title": "Aserrí"},
						{"title": "Tarbaca"},
						{"title": "Vuelta de Jorco"},
						{"title": "San Gabriel"},
						{"title": "La Legua"},
						{"title": "Monterrey"},
						{"title": "Salitrillos"}
					]
				},
				{
					"title": "Mora",
					"distritos": [
						{"title": "Colón"},
						{"title": "Guayabo"},
						{"title": "Tabarcia"},
						{"title": "Piedras Negras"},
						{"title": "Picagres"},
						{"title": "Caris"},
						{"title": "Quitirrisí"}
					]
				},
				{
					"title": "Goicoechea",
					"distritos": [
						{"title": "Guadalupe"},
						{"title": "San Francisco"},
						{"title": "Calle Blancos"},
						{"title": "Mata de Plátano"},
						{"title": "Ipís"},
						{"title": "Rancho Redondo"},
						{"title": "Purral"}
					]
				},
				{
					"title": "Santa Ana",
					"distritos": [
						{"title": "Santa Ana"},
						{"title": "Salitral"},
						{"title": "Pozos"},
						{"title": "Uruca"},
						{"title": "Piedades"},
						{"title": "Brasil"}
					]
				},
				{
					"title": "Alajuelita",
					"distritos": [
						{"title": "Alajuelita"},
						{"title": "San Josecito"},
						{"title": "San Antonio"},
						{"title": "Concepción"},
						{"title": "San Felipe"}
					]
				},
				{
					"title": "Coronado",
					"distritos": [
						{"title": "San Isidro"},
						{"title": "San Rafael"},
						{"title": "Dulce Nombre de Jesús"},
						{"title": "Patalillo"},
						{"title": "Cascajal"}
					]
				},
				{
					"title": "Acosta",
					"distritos": [
						{"title": "San Ignacio"},
						{"title": "Guaitil"},
						{"title": "Palmichal"},
						{"title": "Cangrejal"},
						{"title": "Sabanillas"}
					]
				},
				{
					"title": "Tibás",
					"distritos": [
						{"title": "San Juan"},
						{"title": "Cinco Esquinas"},
						{"title": "Anselmo Llorente"},
						{"title": "León XIII"},
						{"title": "Colima"}
					]
				},
				{
					"title": "Moravia",
					"distritos": [
						{"title": "San Vicente"},
						{"title": "San Jerónimo"},
						{"title": "Trinidad"}
					]
				},
				{
					"title": "Montes de Oca",
					"distritos": [
						{"title": "San Pedro"},
						{"title": "Sabanilla"},
						{"title": "Mercedes"},
						{"title": "San Rafael"}
					]
				},
				{
					"title": "Turrubares",
					"distritos": [
						{"title": "San Pablo"},
						{"title": "San Pedro"},
						{"title": "San Juan de Mata"},
						{"title": "San Luis"},
						{"title": "Cárara"}
					]
				},
				{
					"title": "Dota",
					"distritos": [
						{"title": "Santa María"},
						{"title": "Jardín"},
						{"title": "Copey"}
					]
				},
				{
					"title": "Curridabat",
					"distritos": [
						{"title": "Curridabat"},
						{"title": "Granadilla"},
						{"title": "Sánchez"},
						{"title": "Tirrases"}
					]
				},
				{
					"title": "Perez Zeledón",
					"distritos": [
						{"title": "San Isidro de el General"},
						{"title": "General"},
						{"title": "Daniel Flores"},
						{"title": "Rivas"},
						{"title": "San Pedro"},
						{"title": "Platanares"},
						{"title": "Pejibaye"},
						{"title": "Cajón"},
						{"title": "Barú"},
						{"title": "Río Nuevo"},
						{"title": "Páramo"},
						{"title": "La Amistad"}
					]
				},
				{
					"title": "León Cortés",
					"distritos": [
						{"title": "San Pablo"},
						{"title": "San Andrés"},
						{"title": "Llano Bonito"},
						{"title": "San Isidro"},
						{"title": "Santa Cruz"},
						{"title": "San Antonio"}
					]
				}
			]
		},
		{
			"title": "Alajuela",
			"cantones": [
				{
					"title": "Alajuela",
					"distritos": [
						{"title": "Alajuela"},
						{"title": "San José"},
						{"title": "Carrizal"},
						{"title": "San Antonio"},
						{"title": "Guácima"},
						{"title": "San Isidro"},
						{"title": "Sabanilla"},
						{"title": "San Rafael"},
						{"title": "Río Segundo"},
						{"title": "Desamparados"},
						{"title": "Turrucares"},
						{"title": "Tambor"},
						{"title": "La Garita"},
						{"title": "Sarapiquí"}
					]
				},
				{
					"title": "San Ramón",
					"distritos": [
						{"title": "San Ramón"},
						{"title": "Santiago"},
						{"title": "San Juan"},
						{"title": "Piedades Norte"},
						{"title": "Piedades Sur"},
						{"title": "San Rafael"},
						{"title": "San Isidro"},
						{"title": "Angeles"},
						{"title": "Alfaro"},
						{"title": "Volio"},
						{"title": "Concepción"},
						{"title": "Zapotal"},
						{"title": "San Isidro de Peñas Blancas"},
						{"title": "San Lorenzo"}
					]
				},
				{
					"title": "Grecia",
					"distritos": [
						{"title": "Grecia"},
						{"title": "San Isidro"},
						{"title": "San José"},
						{"title": "San Roque"},
						{"title": "Tacares"},
						{"title": "Puente Piedra"},
						{"title": "Bolívar"}
					]
				},
				{
					"title": "San Mateo",
					"distritos": [
						{"title": "San Mateo"},
						{"title": "Desmonte"},
						{"title": "Jesús María"},
						{"title": "Labrador"}
					]
				},
				{
					"title": "Atenas",
					"distritos": [
						{"title": "Atenas"},
						{"title": "Jesús"},
						{"title": "Mercedes"},
						{"title": "San Isidro"},
						{"title": "Concepción"},
						{"title": "San José"},
						{"title": "Santa Eulalia"},
						{"title": "Escobal"}
					]
				},
				{
					"title": "Naranjo",
					"distritos": [
						{"title": "Naranjo"},
						{"title": "San Miguel"},
						{"title": "San José"},
						{"title": "Cirrí Sur"},
						{"title": "San Jerónimo"},
						{"title": "San Juan"},
						{"title": "Rosario"},
						{"title": "Palmitos"}
					]
				},
				{
					"title": "Palmares",
					"distritos": [
						{"title": "Palmares"},
						{"title": "Zaragoza"},
						{"title": "Buenos Aires"},
						{"title": "Santiago"},
						{"title": "Candelaria"},
						{"title": "Esquipulas"},
						{"title": "La Granja"}
					]
				},
				{
					"title": "Poas",
					"distritos": [
						{"title": "San Pedro"},
						{"title": "San Juan"},
						{"title": "San Rafael"},
						{"title": "Carrillos"},
						{"title": "Sabana Redonda"}
					]
				},
				{
					"title": "Orotina",
					"distritos": [
						{"title": "Orotina"},
						{"title": "Mastate"},
						{"title": "Hacienda Vieja"},
						{"title": "Coyolar"},
						{"title": "Ceiba"}
					]
				},
				{
					"title": "San Carlos",
					"distritos": [
						{"title": "Quesada"},
						{"title": "Florencia"},
						{"title": "Buenavista"},
						{"title": "Aguas Zarcas"},
						{"title": "Venecia"},
						{"title": "Pital"},
						{"title": "Fortuna"},
						{"title": "Tigra"},
						{"title": "Palmera"},
						{"title": "Venado"},
						{"title": "Cutris"},
						{"title": "Monterrey"},
						{"title": "Pocosol"}
					]
				},
				{
					"title": "Zarcero",
					"distritos": [
						{"title": "Zarcero"},
						{"title": "Laguna"},
						{"title": "Tapezco"},
						{"title": "Guadalupe"},
						{"title": "Palmira"},
						{"title": "Zapote"},
						{"title": "Las Brisas"}
					]
				},
				{
					"title": "Valverde Vega",
					"distritos": [
						{"title": "Sarchí Norte"},
						{"title": "Sarchí Sur"},
						{"title": "Toro Amarillo"},
						{"title": "San Pedro"},
						{"title": "Rodríguez"}
					]
				},
				{
					"title": "Upala",
					"distritos": [
						{"title": "Upala"},
						{"title": "Aguas Claras"},
						{"title": "San José"},
						{"title": "Bijagua"},
						{"title": "Delicias"},
						{"title": "Dos Ríos"},
						{"title": "Yolillal"},
						{"title": "Canalete"}
					]
				},
				{
					"title": "Los Chiles",
					"distritos": [
						{"title": "Los Chiles"},
						{"title": "Caño Negro"},
						{"title": "Amparo"},
						{"title": "San Jorge"}
					]
				},
				{
					"title": "Guatuso",
					"distritos": [
						{"title": "San Rafael"},
						{"title": "Buenavista"},
						{"title": "Cote"},
						{"title": "Katira"}
					]
				},
				{
					"title": "Río Cuarto",
					"distritos": [
						{"title": "Río Cuarto"},
						{"title": "Santa Isabel"},
						{"title": "Santa Rita"}
					]
				}
			]
		},
		{
			"title": "Cartago",
			"cantones": [
				{
					"title": "Cartago",
					"distritos": [
						{"title": "Oriental"},
						{"title": "Occidental"},
						{"title": "Carmen"},
						{"title": "San Nicolás"},
						{"title": "Aguacaliente"},
						{"title": "Guadalupe"},
						{"title": "Corralillo"},
						{"title": "Tierra Blanca"},
						{"title": "Dulce Nombre"},
						{"title": "Llano Grande"},
						{"title": "Quebradilla"}
					]
				},
				{
					"title": "Paraíso",
					"distritos": [
						{"title": "Paraíso"},
						{"title": "Santiago"},
						{"title": "Orosi"},
						{"title": "Cachí"},
						{"title": "Los Llanos de Santa Lucía"}
					]
				},
				{
					"title": "La Unión",
					"distritos": [
						{"title": "Tres Ríos"},
						{"title": "San Diego"},
						{"title": "San Juan"},
						{"title": "San Rafael"},
						{"title": "Concepción"},
						{"title": "Dulce Nombre"},
						{"title": "San Ramón"},
						{"title": "Río Azul"}
					]
				},
				{
					"title": "Jiménez",
					"distritos": [
						{"title": "Juan Viñas"},
						{"title": "Tucurrique"},
						{"title": "Pejibaye"}
					]
				},
				{
					"title": "Turrialba",
					"distritos": [
						{"title": "Turrialba"},
						{"title": "La Suiza"},
						{"title": "Peralta"},
						{"title": "Santa Cruz"},
						{"title": "Santa Teresita"},
						{"title": "Pavones"},
						{"title": "Tuis"},
						{"title": "Tayutic"},
						{"title": "Santa Rosa"},
						{"title": "Tres Equis"},
						{"title": "La Isabel"},
						{"title": "Chirripó"}
					]
				},
				{
					"title": "Alvarado",
					"distritos": [
						{"title": "Pacayas"},
						{"title": "Cervantes"},
						{"title": "Capellades"}
					]
				},
				{
					"title": "Oreamuno",
					"distritos": [
						{"title": "San Rafael"},
						{"title": "Cot"},
						{"title": "Potrero Cerrado"},
						{"title": "Cipreses"},
						{"title": "Santa Rosa"}
					]
				},
				{
					"title": "El Guarco",
					"distritos": [
						{"title": "El Tejar"},
						{"title": "San Isidro"},
						{"title": "Tobosi"},
						{"title": "Patio de Agua"}
					]
				}
			]
		},
		{
			"title": "Heredia",
			"cantones": [
				{
					"title": "Heredia",
					"distritos": [
						{"title": "Heredia"},
						{"title": "Mercedes"},
						{"title": "San Francisco"},
						{"title": "Ulloa"},
						{"title": "Varablanca"}
					]
				},
				{
					"title": "Barva",
					"distritos": [
						{"title": "Barva"},
						{"title": "San Pedro"},
						{"title": "San Pablo"},
						{"title": "San Roque"},
						{"title": "Santa Lucía"},
						{"title": "San José de la Montaña"}
					]
				},
				{
					"title": "Santo Domingo",
					"distritos": [
						{"title": "Santo Domingo"},
						{"title": "San Vicente"},
						{"title": "San Miguel"},
						{"title": "Paracito"},
						{"title": "Santo Tomás"},
						{"title": "Santa Rosa"},
						{"title": "Tures"},
						{"title": "Pará"}
					]
				},
				{
					"title": "Santa Bárbara",
					"distritos": [
						{"title": "Santa Bárbara"},
						{"title": "San Pedro"},
						{"title": "San Juan"},
						{"title": "Jesús"},
						{"title": "Santo Domingo del Roble"},
						{"title": "Puraba"}
					]
				},
				{
					"title": "San Rafael",
					"distritos": [
						{"title": "San Rafael"},
						{"title": "San Josecito"},
						{"title": "Santiago"},
						{"title": "Angeles"},
						{"title": "Concepción"}
					]
				},
				{
					"title": "San Isidro",
					"distritos": [
						{"title": "San Isidro"},
						{"title": "San José"},
						{"title": "Concepción"},
						{"title": "San Francisco"}
					]
				},
				{
					"title": "Belén",
					"distritos": [
						{"title": "San Antonio"},
						{"title": "La Ribera"},
						{"title": "Asunción"}
					]
				},
				{
					"title": "Flores",
					"distritos": [
						{"title": "San Joaquín"},
						{"title": "Barrantes"},
						{"title": "Llorente"}
					]
				},
				{
					"title": "San Pablo",
					"distritos": [
						{"title": "San Pablo"},
						{"title": "Rincón de Sabanilla"}
					]
				},
				{
					"title": "Sarapiquí",
					"distritos": [
						{"title": "Puerto Viejo"},
						{"title": "La Virgen"},
						{"title": "Horquetas"},
						{"title": "Llanuras de Gaspar"},
						{"title": "Cureña"}
					]
				}
			]
		},
		{
			"title": "Guanacaste",
			"cantones": [
				{
					"title": "Liberia",
					"distritos": [
						{"title": "Liberia"},
						{"title": "Cañas Dulces"},
						{"title": "Mayorga"},
						{"title": "Nacascolo"},
						{"title": "Curubande"}
					]
				},
				{
					"title": "Nicoya",
					"distritos": [
						{"title": "Nicoya"},
						{"title": "Mansión"},
						{"title": "San Antonio"},
						{"title": "Quebrada Honda"},
						{"title": "Sámara"},
						{"title": "Nósara"},
						{"title": "Belén de Nosarita"}
					]
				},
				{
					"title": "Santa Cruz",
					"distritos": [
						{"title": "Santa Cruz"},
						{"title": "Bolsón"},
						{"title": "Veintisiete de Abril"},
						{"title": "Tempate"},
						{"title": "Cartagena"},
						{"title": "Cuajiniquil"},
						{"title": "Diriá"},
						{"title": "Cabo Velas"},
						{"title": "Tamarindo"}
					]
				},
				{
					"title": "Bagaces",
					"distritos": [
						{"title": "Bagaces"},
						{"title": "Fortuna"},
						{"title": "Mogote"},
						{"title": "Río Naranjo"}
					]
				},
				{
					"title": "Carrillo",
					"distritos": [
						{"title": "Filadelfia"},
						{"title": "Palmira"},
						{"title": "Sardinal"},
						{"title": "Belén"}
					]
				},
				{
					"title": "Cañas",
					"distritos": [
						{"title": "Cañas"},
						{"title": "Palmira"},
						{"title": "San Miguel"},
						{"title": "Bebedero"},
						{"title": "Porozal"}
					]
				},
				{
					"title": "Abangares",
					"distritos": [
						{"title": "Juntas"},
						{"title": "Sierra"},
						{"title": "San Juan"},
						{"title": "Colorado"}
					]
				},
				{
					"title": "Tilarán",
					"distritos": [
						{"title": "Tilarán"},
						{"title": "Quebrada Grande"},
						{"title": "Tronadora"},
						{"title": "Santa Rosa"},
						{"title": "Líbano"},
						{"title": "Tierras Morenas"},
						{"title": "Arenal"}
					]
				},
				{
					"title": "Nandayure",
					"distritos": [
						{"title": "Carmona"},
						{"title": "Santa Rita"},
						{"title": "Zapotal"},
						{"title": "San Pablo"},
						{"title": "Porvenir"},
						{"title": "Bejuco"}
					]
				},
				{
					"title": "La Cruz",
					"distritos": [
						{"title": "La Cruz"},
						{"title": "Santa Cecilia"},
						{"title": "Garita"},
						{"title": "Santa Elena"}
					]
				},
				{
					"title": "Hojancha",
					"distritos": [
						{"title": "Hojancha"},
						{"title": "Monte Romo"},
						{"title": "Puerto Carrillo"},
						{"title": "Huacas"}
					]
				}
			]
		},
		{
			"title": "Puntarenas",
			"cantones": [
				{
					"title": "Puntarenas",
					"distritos": [
						{"title": "Puntarenas"},
						{"title": "Pitahaya"},
						{"title": "Chomes"},
						{"title": "Lepanto"},
						{"title": "Paquera"},
						{"title": "Manzanillo"},
						{"title": "Guacimal"},
						{"title": "Barranca"},
						{"title": "Monte Verde"},
						{"title": "Isla del Coco"},
						{"title": "Cóbano"},
						{"title": "Chacarita"},
						{"title": "Chira"},
						{"title": "Acapulco"},
						{"title": "Roble"},
						{"title": "Arancibia"}
					]
				},
				{
					"title": "Esparza",
					"distritos": [
						{"title": "Espíritu Santo"},
						{"title": "San Juan Grande"},
						{"title": "Macacona"},
						{"title": "San Rafael"},
						{"title": "San Jerónimo"},
						{"title": "Caldera"}
					]
				},
				{
					"title": "Buenos Aires",
					"distritos": [
						{"title": "Buenos Aires"},
						{"title": "Volcán"},
						{"title": "Potrero Grande"},
						{"title": "Boruca"},
						{"title": "Pilas"},
						{"title": "Colinas"},
						{"title": "Chánguena"},
						{"title": "Bioley"},
						{"title": "Brunka"}
					]
				},
				{
					"title": "Montes de Oro",
					"distritos": [
						{"title": "Miramar"},
						{"title": "Unión"},
						{"title": "San Isidro"}
					]
				},
				{
					"title": "Osa",
					"distritos": [
						{"title": "Puerto Cortés"},
						{"title": "Palmar"},
						{"title": "Sierpe"},
						{"title": "Bahía Ballena"},
						{"title": "Piedras Blancas"},
						{"title": "Bahía Drake"}
					]
				},
				{
					"title": "Quepos",
					"distritos": [
						{"title": "Quepos"},
						{"title": "Savegre"},
						{"title": "Naranjito"}
					]
				},
				{
					"title": "Golfito",
					"distritos": [
						{"title": "Golfito"},
						{"title": "Puerto Jiménez"},
						{"title": "Guaycará"},
						{"title": "Pavón"}
					]
				},
				{
					"title": "Coto Brus",
					"distritos": [
						{"title": "San Vito"},
						{"title": "Sabalito"},
						{"title": "Agua Buena"},
						{"title": "Limoncito"},
						{"title": "Pittier"},
						{"title": "Gutiérrez Brown"}
					]
				},
				{
					"title": "Parrita",
					"distritos": [
						{"title": "Parrita"}
					]
				},
				{
					"title": "Corredores",
					"distritos": [
						{"title": "Corredores"},
						{"title": "La Cuesta"},
						{"title": "Paso Canoas"},
						{"title": "Laurel"}
					]
				},
				{
					"title": "Garabito",
					"distritos": [
						{"title": "Jacó"},
						{"title": "Tárcoles"}
					]
				}
			]
		},
		{
			"title": "Limón",
			"cantones": [
				{
					"title": "Limón",
					"distritos": [
						{"title": "Limón"},
						{"title": "Valle La Estrella"},
						{"title": "Río Blanco"},
						{"title": "Matama"}
					]
				},
				{
					"title": "Pococí",
					"distritos": [
						{"title": "Guápiles"},
						{"title": "Jiménez"},
						{"title": "Rita"},
						{"title": "Roxana"},
						{"title": "Cariari"},
						{"title": "Colorado"},
						{"title": "La Colonia"}
					]
				},
				{
					"title": "Siquirres",
					"distritos": [
						{"title": "Siquirres"},
						{"title": "Pacuarito"},
						{"title": "Florida"},
						{"title": "Germania"},
						{"title": "Cairo"},
						{"title": "Alegría"}
					]
				},
				{
					"title": "Talamanca",
					"distritos": [
						{"title": "Bratsi"},
						{"title": "Sixaola"},
						{"title": "Cahuita"},
						{"title": "Telire"}
					]
				},
				{
					"title": "Matina",
					"distritos": [
						{"title": "Matina"},
						{"title": "Batán"},
						{"title": "Carrandí"}
					]
				},
				{
					"title": "Guácimo",
					"distritos": [
						{"title": "Guácimo"},
						{"title": "Mercedes"},
						{"title": "Pocora"},
						{"title": "Río Jiménez"},
						{"title": "Duacarí"}
					]
				}
			]
		}
	]
}'''


def get_provincias():
    """
    Devuelve una lista con el nombre de las provincias de Costa Rica
    """

    # Crear una lista vacía para almacenar las provincias
    salida = []

    # Cargar las ubicaciones del Objeto JSON con provincias, cantones y distritos de CR.
    f = json.loads(ubicaciones)

    # Iterar a través de las provincias en el archivo JSON
    for provincia in f['provincias']:
        # Agregar el nombre de la provincia a la lista de salida
        salida.append(provincia['title'])

    # Devolver la lista de salida
    return salida


def get_cantones(p_provincia):
    """
    Devuelve una lista con el nombre de los cantones de Costa Rica, recibiendo como parámetro el nombre de la provincia
    """
    # Crear una lista vacía para almacenar los cantones
    salida = []

    # Cargar el archivo JSON de ubicaciones
    f = json.loads(ubicaciones)

    # Iterar a través de las provincias en el archivo JSON
    for i in f['provincias']:
        # Almacenar el título de la provincia actual
        provincia = i['title']

        # Verificar si la provincia actual es la provincia buscada, de acuerdo al parametro p_provincia
        if provincia == p_provincia:
            # Iterar a través de los cantones en la provincia especificada
            for f in i['cantones']:
                # Almacenar el título del cantón actual
                canton = f['title']

                # Agregar el título del cantón a la lista de salida
                salida.append(canton)
            # Devolver la lista de salida con todos los cantones de la provincia
            return salida

    # Devolver la lista de salida vacía si la provincia especificada no se encuentra
    return salida


def get_distritos(p_provincia, p_canton):
    """
    Devuelve una lista con el nombre de los distritos de Costa Rica, recibiendo como parámetro el nombre de la provincia y el cantón
    """
	# Crear una lista vacía para almacenar los distritos
    salida = []

	# Cargar el archivo JSON de ubicaciones
    f = json.loads(ubicaciones)

	# Iterar a través de las provincias en el archivo JSON
    for item in f['provincias']:
		# Almacenar el título de la provincia actual
        provincia = item['title']
        if provincia == p_provincia:
			# Iterar a través de los cantones en el archivo JSON
            for f in item['cantones']:
				# Almacenar el título del cantón actual
                canton = f['title']
                if canton == p_canton:
					# Iterar a través de los distritos en el archivo JSON
                    for e in f['distritos']:
						# Almacenar el título del distrito
                        distrito = e['title']
						# Agregar el título del distrito a la lista de salida
                        salida.append(distrito)
					# Devolver la lista de salida con todos los cantones de la provincia
                    return salida
	# Devolver la lista de salida vacía si la provincia especificada no se encuentra
    return salida


def imprimir_estadisticas_listas():
    """
    Imprime el número de elementos en las listas de nombres masculinos, nombres femeninos y apellidos.
    Returns:
    None
    """
    # Imprime la cantidad de nombres masculinos en la lista "nombres_masculinos".
    print("Nombres masculinos:", len(nombres_masculinos))
    # Imprime la cantidad de nombres femeninos en la lista "nombres_femeninos".
    print("Nombres femeninos:", len(nombres_femeninos))
    # Imprime la cantidad de apellidos en la lista "apellidos".
    print("Apellidos:", len(apellidos))


def generar_nombre(sexo=None, nombre_compuesto=False):
	"""
	Esta función genera un nombre aleatorio a partir de dos listas de nombres y apellidos. El parámetro sexo es opcional 
	y puede ser "m" para masculino o "f" para femenino. El parámetro nombre_compuesto indica si el nombre generado 
	será compuesto o no. Si el parámetro sexo no se especifica, la función generará un nombre aleatorio de cualquier 
	sexo con o sin nombre compuesto.
	"""

	# Si no se especifica el sexo, se genera una persona de sexo aleatorio, con nombre compuesto o no.
	if sexo == None:
		# Elegir una opción aleatoria
		opt = r.randint(0, 3)
		if opt == 0:
			return generar_nombre(sexo='m', nombre_compuesto=False)
		if opt == 1:
			return generar_nombre(sexo='f', nombre_compuesto=False)
		if opt == 2:
			return generar_nombre(sexo='m', nombre_compuesto=True)
		if opt == 3:
			return generar_nombre(sexo='f', nombre_compuesto=True)
	else:

		# Obtener dos apellidos aleatorios de la lista de apellidos
		apellido1 = apellidos[r.randint(0, len(apellidos)-1)]
		apellido2 = apellidos[r.randint(0, len(apellidos)-1)]

		# Generar nombre femenino
		if sexo.lower() == "f" or sexo.lower() == "F":
			if not nombre_compuesto:
				nombre = nombres_femeninos[r.randint(0, len(nombres_femeninos)-1)]
			else:
				# Concatenar dos nombres femeninos
				nombre = nombres_femeninos[r.randint(0, len(
					nombres_femeninos)-1)] + ' ' + nombres_femeninos[r.randint(0, len(nombres_femeninos)-1)]
			return nombre + " " + apellido1 + " " + apellido2

		# Generar nombre masculino
		if sexo.lower() == "m" or sexo.lower() == "M":
			if not nombre_compuesto:
				nombre = nombres_masculinos[r.randint(
					0, len(nombres_masculinos)-1)]
			else:
				# Concatenar dos nombres masculinos
				nombre = nombres_masculinos[r.randint(0, len(
					nombres_masculinos)-1)] + ' ' + nombres_masculinos[r.randint(0, len(nombres_masculinos)-1)]
			return nombre + " " + apellido1 + " " + apellido2


def generar_cedula():
	"""
    Esta función genera un número de cédula aleatorio para una persona en Costa Rica. 
    La cédula está formada por 3 partes: una provincia (1 a 8), un número (0 a 1600 o 0 a 999) y un número (0 a 9999).
    """
	provincia = r.randint(1, 8)

	# El número de la cédula para la provincia 1 puede tener hasta 1600 dígitos
	if provincia == 1:
		return str(provincia) + "-" + str(r.randint(0, 1600)).zfill(4) + "-" + str(r.randint(0, 9999)).zfill(4)	
	# El número de la cédula para el resto de las provincias solo puede tener hasta 999 dígitos
	else:
		return str(provincia) + "-" + str(r.randint(0, 999)).zfill(4) + "-" + str(r.randint(0, 9999)).zfill(4)


def generar_telefono(tipo=None):
	"""
	Devuelve un numero de telefono generado aleatoreamente, si el tipo es 'c' es celular, y 'f' es telefono fijo
	"""
	# Verifica si tipo es igual a "c" y genera un número de teléfono celular
	if tipo == 'c':
		return '8' + str(r.randint(3, 9)) + str(r.randint(0, 99)).zfill(2) + "-" + str(r.randint(0, 9999)).zfill(4)

	# Verifica si tipo es igual a "f" y genera un número de teléfono fijo
	if tipo == 'f':
		return '2' + str(r.randint(3, 9)) + str(r.randint(0, 99)).zfill(2) + "-" + str(r.randint(0, 9999)).zfill(4)

    # Si tipo es None, se genera un número de teléfono aleatoriamente entre celular y fijo
	if tipo == None:
		random = r.randint(0, 1)
		if random == 0:
			return generar_telefono('c')
		else:
			return generar_telefono('f')


def generar_provincia():
	"""
	Devuelve una provincia aleatoria de la lista de provincias disponibles
	"""
	return r.choice(get_provincias())


def generar_canton(provincia):
	"""
	Devuelve un cantón aleatorio de la lista de cantones disponibles
	"""
	return r.choice(get_cantones(provincia))


def generar_distrito(provincia, canton):
	"""
	Devuelve un distrito aleatorio de la lista de distritos disponibles
	"""
	return r.choice(get_distritos(provincia, canton))


def generar_coordinada():
	"""
	Devuelve un coordenada de la lista de coordinadas disponibles
	"""
	coordenadas = ["Norte", "Sur", "Este", "Oeste"]
	return r.choice(coordenadas)


def generar_direccion(provincia=None, canton=None):
	"""
	Devuelve una dirección aleatoria en formato de texto utilizando funciones auxiliares generar_coordinada, generar_provincia, 
	generar_canton y generar_distrito. La dirección generada incluye la cantidad de metros en bloques de 100 de la ubicación,
	la coordenada de la ubicación (Norte, Sur, Este, Oeste), el tipo de lugar (elegido de la lista lugares), el nombre del
	lugar (elegido de la lista nombre_lugares), el distrito, el cantón y la provincia.
	Puede recibir la provincia y canton para generar la dirección.
	"""
    # Genera un número aleatorio entre 100 y 800 para la cantidad de metros de una ubicación
	cantidad = r.randint(100, 800)
    # Convierte el número generado a una cadena de caracteres y le aplica una operación módulo para obtener los metros
    # en bloques de 100 (ej. 500 -> 500, 550 -> 500)
	metros = str(cantidad - (cantidad % 100))
    # Llama a la función generar_coordinada() para obtener una coordenada (Norte, Sur, Este, Oeste)
	coordenada = generar_coordinada()

    # Llama a la función generar_provincia() para obtener una provincia
	if provincia is None:
		provincia = generar_provincia()

	if canton is None:
    # Llama a la función generar_canton() con la provincia obtenida como argumento para obtener un cantón
		canton = generar_canton(provincia)

	# Llama a la función generar_distrito() con la provincia y cantón obtenidos como argumentos para obtener un distrito
	distrito = generar_distrito(provincia, canton)
    # Devuelve la dirección generada como una cadena de caracteres con la siguiente estructura:
    # metros + " " + coordenada + " " + lugar elegido al azar de la lista lugares + " " + 
	# nombre de lugar elegido al azar de la lista nombre_lugares + ", " + distrito + ", " + canton + ", " + provincia
	return metros + " " + coordenada + " " + r.choice(lugares) + " " + r.choice(nombre_lugares) + ", " + distrito + ", " + canton + ", " + provincia


def generar_salario(min=330000, max=2500000):
	"""
	Devuelve un salario aleatorio entre 330,000 y 2,500,000 colones
	"""
	return str(r.randint(min, max))


def generar_persona(p_cantidad=1, p_sexo=None):
	"""
	Devuelve una lista de datos aleatorios para una persona especificada por la cantidad en el parámetro "p_cantidad".
	La información generada incluye un nombre, un número de cédula, una dirección, una provincia, un cantón, 
	un distrito, un salario y un número de teléfono. También se proporciona un género opcional "p_sexo" 
	para la generación del nombre. La función devuelve la lista completa de información generada para cada persona.
	"""

    # Inicializa una lista vacía para almacenar la información generada
	salida = []

    # Repite el proceso para el número de individuos especificados en el parametro p_cantidad
	for i in range(p_cantidad):
        # Genera un nombre usando el género proporcionado
		nombre = generar_nombre(p_sexo)
        # Genera un número de cédula aleatorio
		cedula = generar_cedula()
        # Genera una provincia
		provincia = generar_provincia()
        # Genera un cantón basado en la provincia generada
		canton = generar_canton(provincia)
        # Genera un distrito basado en la provincia y cantón generados
		distrito = generar_distrito(provincia, canton)
		# Genera una dirección
		direccion = generar_direccion(provincia=provincia,canton=canton)
        # Genera un salario
		salario = generar_salario()
        # Genera un número de teléfono
		telefono = generar_telefono()
        # Agrega toda la información generada para este individuo a la lista de salida
		salida.append([cedula, nombre, telefono, provincia,
                      canton, distrito, direccion, salario])
	return salida
