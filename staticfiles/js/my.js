URL = 'http://localhost:8000/'
//URL = 'https://www.cartrek.us/'

function browse_slider() {
    var slider = document.getElementById('dtime_range');
    var label = document.getElementById('dlabel');
    var check = document.getElementById('dtime');

    slider.oninput = function() {
        var time = parseInt(this.value) % 12;
        check.checked = true;
        if (time == 0) {
            time = 12;
        }
        label.innerHTML = 'Departure Time: ' + time.toString() + ':00';
        if (parseInt(this.value) > 11) {
            label.innerHTML += 'pm';
        } else {
            label.innerHTML +='am';
        }
    };
}

function post_sliders() {
    var pickup = document.getElementById('id_pickup_radius');
    var dropoff = document.getElementById('id_dropoff_radius');
    var plabel = document.getElementById('pdl');
    var dlabel = document.getElementById('ddl');
    var pcheck = document.getElementById('id_pickup');
    var dcheck = document.getElementById('id_dropoff');

    pickup.oninput = function() {
        pcheck.checked = true;
        plabel.innerHTML = 'Max distance: ';
        plabel.innerHTML += this.value;
        plabel.innerHTML += ' miles';
    };

    dropoff.oninput = function() {
        dcheck.checked = true;
        dlabel.innerHTML = 'Max distance: ';
        dlabel.innerHTML += this.value;
        dlabel.innerHTML += ' miles';
    };
}

function succ(pos) {
    var city = document.getElementById('id_from_city');
    var state = document.getElementById('id_from_state');
    var lat = pos.coords.latitude;
    var lng = pos.coords.longitude;
    var geo_api = 'https://nominatim.openstreetmap.org/reverse?format=json'
    var states = [
        {
            "name": "Alabama",
            "abbreviation": "AL"
        },
        {
            "name": "Alaska",
            "abbreviation": "AK"
        },
        {
            "name": "American Samoa",
            "abbreviation": "AS"
        },
        {
            "name": "Arizona",
            "abbreviation": "AZ"
        },
        {
            "name": "Arkansas",
            "abbreviation": "AR"
        },
        {
            "name": "California",
            "abbreviation": "CA"
        },
        {
            "name": "Colorado",
            "abbreviation": "CO"
        },
        {
            "name": "Connecticut",
            "abbreviation": "CT"
        },
        {
            "name": "Delaware",
            "abbreviation": "DE"
        },
        {
            "name": "District Of Columbia",
            "abbreviation": "DC"
        },
        {
            "name": "Federated States Of Micronesia",
            "abbreviation": "FM"
        },
        {
            "name": "Florida",
            "abbreviation": "FL"
        },
        {
            "name": "Georgia",
            "abbreviation": "GA"
        },
        {
            "name": "Guam",
            "abbreviation": "GU"
        },
        {
            "name": "Hawaii",
            "abbreviation": "HI"
        },
        {
            "name": "Idaho",
            "abbreviation": "ID"
        },
        {
            "name": "Illinois",
            "abbreviation": "IL"
        },
        {
            "name": "Indiana",
            "abbreviation": "IN"
        },
        {
            "name": "Iowa",
            "abbreviation": "IA"
        },
        {
            "name": "Kansas",
            "abbreviation": "KS"
        },
        {
            "name": "Kentucky",
            "abbreviation": "KY"
        },
        {
            "name": "Louisiana",
            "abbreviation": "LA"
        },
        {
            "name": "Maine",
            "abbreviation": "ME"
        },
        {
            "name": "Marshall Islands",
            "abbreviation": "MH"
        },
        {
            "name": "Maryland",
            "abbreviation": "MD"
        },
        {
            "name": "Massachusetts",
            "abbreviation": "MA"
        },
        {
            "name": "Michigan",
            "abbreviation": "MI"
        },
        {
            "name": "Minnesota",
            "abbreviation": "MN"
        },
        {
            "name": "Mississippi",
            "abbreviation": "MS"
        },
        {
            "name": "Missouri",
            "abbreviation": "MO"
        },
        {
            "name": "Montana",
            "abbreviation": "MT"
        },
        {
            "name": "Nebraska",
            "abbreviation": "NE"
        },
        {
            "name": "Nevada",
            "abbreviation": "NV"
        },
        {
            "name": "New Hampshire",
            "abbreviation": "NH"
        },
        {
            "name": "New Jersey",
            "abbreviation": "NJ"
        },
        {
            "name": "New Mexico",
            "abbreviation": "NM"
        },
        {
            "name": "New York",
            "abbreviation": "NY"
        },
        {
            "name": "North Carolina",
            "abbreviation": "NC"
        },
        {
            "name": "North Dakota",
            "abbreviation": "ND"
        },
        {
            "name": "Northern Mariana Islands",
            "abbreviation": "MP"
        },
        {
            "name": "Ohio",
            "abbreviation": "OH"
        },
        {
            "name": "Oklahoma",
            "abbreviation": "OK"
        },
        {
            "name": "Oregon",
            "abbreviation": "OR"
        },
        {
            "name": "Palau",
            "abbreviation": "PW"
        },
        {
            "name": "Pennsylvania",
            "abbreviation": "PA"
        },
        {
            "name": "Puerto Rico",
            "abbreviation": "PR"
        },
        {
            "name": "Rhode Island",
            "abbreviation": "RI"
        },
        {
            "name": "South Carolina",
            "abbreviation": "SC"
        },
        {
            "name": "South Dakota",
            "abbreviation": "SD"
        },
        {
            "name": "Tennessee",
            "abbreviation": "TN"
        },
        {
            "name": "Texas",
            "abbreviation": "TX"
        },
        {
            "name": "Utah",
            "abbreviation": "UT"
        },
        {
            "name": "Vermont",
            "abbreviation": "VT"
        },
        {
            "name": "Virgin Islands",
            "abbreviation": "VI"
        },
        {
            "name": "Virginia",
            "abbreviation": "VA"
        },
        {
            "name": "Washington",
            "abbreviation": "WA"
        },
        {
            "name": "West Virginia",
            "abbreviation": "WV"
        },
        {
            "name": "Wisconsin",
            "abbreviation": "WI"
        },
        {
            "name": "Wyoming",
            "abbreviation": "WY"
        }
    ];
    var xhr = new XMLHttpRequest();

    xhr.open('GET', geo_api + '&lat=' + lat + '&lon=' + lng, true);
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var addr = JSON.parse(this.response).address;
            city.value = addr.town || addr.city || addr.borough || '';
			s = states.find(function(elem) { return elem.name == addr.state });
            state.value = s.abbreviation;
        }
    };
    xhr.send();
}

function fail(pos) {
    console.log('fail');
}

function geolocate() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(succ, fail);
    }
}

function msg_count(user) {
    var inbox = document.getElementById('inbox');
    var xhr = new XMLHttpRequest();

    xhr.open('POST', URL + 'profiles/msg_count/', true);
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if (this.response != 0) {
                inbox.innerHTML += ' ( ' + this.response + ' )';
            }
        }
    };
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify({user: user}));
}

function affiliate() {
    var input = document.getElementById('org');
    var selectval = document.getElementById('id_affiliation').value;
    var org = document.querySelector(`[value="${selectval}"]`).innerHTML;
    var label = document.getElementById('org_label');
    
    input.style = 'display: block;';
    label.innerHTML = org + ' email for verification:';
}

function browse_dp() {
    if ($('#date')[0].type != 'date') {
        $('#date').datepicker({dateFormat: 'yy-mm-dd'}).val();
    }
}

function post_dp() {
    if ($('#id_date')[0].type != 'date') {
        $('#id_date').datepicker({dateFormat: 'yy-mm-dd'}).val();
    }
}

function show_treks() {
    var treks_btn = document.getElementById('treks_btn');
    var reqs_btn = document.getElementById('reqs_btn');
    var treks_div = document.getElementById('treks');
    var reqs_div = document.getElementById('requests');

    reqs_div.style = 'display: none;';
    treks_div.style= 'display: block;';
    treks_btn.className = 'btn btn-success';
    reqs_btn.className = 'btn btn-outline-success';
}

function show_reqs() {
    var treks_btn = document.getElementById('treks_btn');
    var reqs_btn = document.getElementById('reqs_btn');
    var treks_div = document.getElementById('treks');
    var reqs_div = document.getElementById('requests');

    treks_div.style = 'display: none;';
    reqs_div.style= 'display: block;';
    reqs_btn.className = 'btn btn-success';
    treks_btn.className = 'btn btn-outline-success';
}

function delete_trek(id) {
    var xhr = new XMLHttpRequest();
    var url = URL + 'treks/delete/' + id.toString() + '/';

    xhr.open('GET', url, false);
    xhr.onreadystatechange = function() {
        if (this.readyState != 4 || this.status != 200) {
            console.log(this.response);
        }
    };

    if (confirm('Are you sure?')) {
        xhr.send();
        location.reload();
    }
}

function leave_trek(id) {
    var xhr = new XMLHttpRequest();
    var url = URL + 'treks/leave/' + id.toString() + '/';

    xhr.open('GET', url, false);
    xhr.onreadystatechange = function() {
        if (this.readyState != 4 || this.status != 200) {
            console.log(this.response);
        }
    };

    if (confirm('Are you sure?')) {
        xhr.send();
        location.reload();
    }
}
