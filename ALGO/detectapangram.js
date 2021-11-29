// Given a string, detect whether or not it uses the letter a-z at least once
// return true if it is, false if not

function isPangram(string){
    let a_z = "abcdefghijklmnopqrstuvwxyz";
    let str = string.split('');
    
    for(let i=0; i<str.length; i++){
        let s = str[i].toLowerCase();
        a_z = a_z.replace(s, "");
    }
    
    if(a_z.length === 0){
        return true;
    } else {
        return false;
    }
}