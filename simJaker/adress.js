const number = "12345678900";
const byte_list = [];

// DA (Destination Address) length
let da_len = number.length;
byte_list.push(da_len);

// DA type of number 0x91: international
byte_list.push(0x91); // international

// DA BCD-digits
let da_nlist = number.split("");
if (da_nlist.length % 2 === 1) {
    da_nlist.push("f");
}
for (let i = 0; i < da_nlist.length; i += 2) {
    let n0 = parseInt(da_nlist[i], 16);
    let n1 = parseInt(da_nlist[i + 1], 16);
    let n = (n1 << 4) + n0;
    byte_list.push(n);
}

console.log(byte_list);

