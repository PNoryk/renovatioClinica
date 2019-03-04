$(function () {
    let clinic = $("#id_clinic_id");

    getUsers(clinic.val());

    clinic.change(function () {
        let clinic = $("#id_clinic_id");

        getUsers(clinic.val())
    });
});

function setUsersIdSelect(data) {
    let htmlText = "";
    let selected = true;

    let element = $("#id_user_id");

    if (data === undefined || data.length === 0) {
        element.html(
            "<option value=''>NoUsers</option>"
        );
        return
    }

    for (let element of data) {
        htmlText += "<option value=\"" + element["id"] + "\"";

        if (selected) {
            htmlText += "selected=\"\"";
            selected = false;
        }

        htmlText += ">" + element["name"] + "</option>";
    }
    element.html(htmlText)
}
//
// function getClinics() {
//     $.ajax({
//         method: "post",
//         url: "https://app.rnova.org/api/public/getClinics",
//         data: {
//             "api_key": "3971c1a15e8449ef7c5e0486471c63cd",
//         },
//         success: function (response) {
//             return response;
//         },
//         error: function () {
//             console.log("getClinics Error");
//         }
//     });
// }
//
// function getProfessions() {
//     $.ajax({
//         method: "POST",
//         url: "https://app.rnova.org/api/public/getProfessions",
//         data: {
//             "api_key": "3971c1a15e8449ef7c5e0486471c63cd",
//         },
//         success: function (response) {
//             if (response.error) {
//                 let data = response["data"];
//                 let msg = data["code"] + " " + data["desc"];
//                 alert(msg);
//                 console.log("Error\n code: {data}\n description: ${data['desc'}");
//             }
//             return response;
//         },
//         error: function () {
//             console.log("getProfessions error");
//         }
//     });
// }


function getUsers(clinic_id, profession_id = 53, role = "", func = setUsersIdSelect) {
    $.ajax({
        method: "POST",
        url: "https://app.rnova.org/api/public/getUsers",
        data: {
            "api_key": "3971c1a15e8449ef7c5e0486471c63cd",
            "clinic_id": clinic_id,
            "profession_id": profession_id,
            "role": role,
        },
        success: function (response) {
            if (response["error"]) {
                func(undefined)
            } else {
                let data = response["data"];
                func(data)
            }
        },
        error: function () {
            console.log("getUsers error");
        }
    })
}
//
// function getSchedule(clinic_id, user_id, time_start, time_end, step) {
//     $.ajax({
//         method: "POST",
//         url: "https://app.rnova.org/api/public/getSchedule",
//         data: {
//             "api_key": "3971c1a15e8449e7c5e0486471c63cd",
//             "clinic_id": clinic_id,
//             "user_id": user_id,
//             "time_start": time_start,
//             "time_end": time_end,
//             "step": step,
//         },
//         success: function (response) {
//             if (checkResponse()) {
//
//                 console.log(response);
//             }
//         },
//         error: function () {
//             console.log("getSchedule error");
//         }
//     })
// }

function checkResponse(response) {
    if (response.error) {
        return false
    }
    return response.data
}

function getResponseError(response) {
    return "Code: " + response.data["code"] + ": " + response.data["desc"]
}