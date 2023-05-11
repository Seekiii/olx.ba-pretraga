<h1>Uzmite OLX.BA artikle u pythonu!</h1>

- Program funkcionise tako sto komunicira sa javnim API-em samog OLX-a i tako dobija informacije o artiklima i kategorijama. 
- Možda nekad u budućnosti updatetam kod sa više mogućnosti i detaljnijim informacijama o artiklima.

<h1>Važno!</h1>

- Ova skripta ne daje detaljne informacije o artiklu sa njegovim opisom, dodatnim informacijama i slično, nego samo informacije koje se nalaze u pretrazi to jest dok pretražujete neke artikle.

<h1>Kako pokrenuti skriptu?</h1>

- Instalirajte ili uzmite kod iz fajla `app.py` i editujte kod onako kako vama treba. (Nemojte koristiti ovo ako ne znate šta radite i za šta vam skripta treba)
- Pokrenite kod komandom `python app.py`

<h1>Ostalo:</h1>

- Informacije koje dobijete u kategoriji (`vozila`):
```json

{
    "data": [
        {
            "category_id": 18,
            "score": null,
            "id": 53100815,
            "type": "single",
            "title": "Audi SQ7 ABT 382 KW",
            "price": 94000,
            "display_price": "94.000 KM",
            "price_max": 0,
            "date": 1683836768,
            "image": "https://d4n0y8dshd77z.cloudfront.net/listings/53100815/sm/img-1683282995-681c6b98151d.jpg",
            "sponsored": 2,
            "available": true,
            "visible": true,
            "shipping": 0,
            "user_type": "user",
            "user_id": 3227530,
            "state": "none",
            "status": "active",
            "location": null,
            "labels": [
                "Dizel",
                227000
            ],
            "listing_type": "sell",
            "special_labels": [
                {
                    "value": "dizel",
                    "label": "Gorivo",
                    "unit": null
                },
                {
                    "value": "227.000",
                    "label": "Kilometra\u017ea",
                    "unit": "km"
                },
                {
                    "value": 2018,
                    "label": "Godi\u0161te",
                    "unit": null
                }
            ]
        }
    ],
    "meta": {
        "total": 65580,
        "last_page": 65580,
        "current_page": 1,
        "per_page": 1,
        "selected_category": 1
    },
    "aggregations": {
        "categories": [
            {
                "id": 1,
                "name": "Vozila",
                "count": 65580,
                "selected": true,
                "sub_categories": [
                    {
                        "id": 18,
                        "name": "Automobili",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 20,
                        "name": "Teretna vozila",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 21,
                        "name": "Motocikli",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 22,
                        "name": "Bicikli",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 426,
                        "name": "Nautika",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 883,
                        "name": "Kamperi",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 884,
                        "name": "Prikolice",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 1040,
                        "name": "Autobusi i minibusi",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 2127,
                        "name": "Motorne sanke",
                        "parent_id": 1,
                        "selected": false
                    },
                    {
                        "id": 2457,
                        "name": "ATV / UTV / Quad",
                        "parent_id": 1,
                        "selected": false
                    }
                ]
            }
        ]
    }
}

```

- Informacije koje dobijete iz pretrage (`bmw f10`):

```json
{
    "data": [
        {
            "category_id": 18,
            "score": null,
            "id": 51912353,
            "type": "single",
            "title": "BMW 530d F10 Full -TOP STANJE-",
            "price": 29990,
            "display_price": "29.990 KM",
            "price_max": 0,
            "date": 1683834547,
            "image": "https://d4n0y8dshd77z.cloudfront.net/listings/51912353/sm/4C7926EF-D3FF-4BA8-8-3c0684ab478a.jpeg",
            "sponsored": 2,
            "available": true,
            "visible": true,
            "shipping": 0,
            "user_type": "shop",
            "user_id": 75163,
            "state": "used",
            "status": "active",
            "location": null,
            "labels": [
                "Dizel",
                241000
            ],
            "listing_type": "sell",
            "special_labels": [
                {
                    "value": "dizel",
                    "label": "Gorivo",
                    "unit": null
                },
                {
                    "value": "241.000",
                    "label": "Kilometra\u017ea",
                    "unit": "km"
                },
                {
                    "value": 2010,
                    "label": "Godi\u0161te",
                    "unit": null
                }
            ]
        }
    ],
    "meta": {
        "total": 6,
        "last_page": 6,
        "current_page": 1,
        "per_page": 1,
        "selected_category": 0
    },
    "aggregations": {
        "categories": [
            {
                "id": 1,
                "name": "Vozila",
                "count": 5,
                "sub_categories": [
                    {
                        "id": 18,
                        "name": "Automobili",
                        "count": 5,
                        "parent_name": "Vozila"
                    }
                ]
            },
            {
                "id": 928,
                "name": "Dijelovi i oprema za vozila",
                "count": 1,
                "sub_categories": [
                    {
                        "id": 941,
                        "name": "Sjedi\u0161ta",
                        "count": 1,
                        "parent_name": "Za automobile"
                    }
                ]
            }
        ]
    }
}
```


