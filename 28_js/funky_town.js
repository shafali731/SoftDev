var factorial = function fact(n) {
  if(n<2){
    return 1;
  }
  else{
    return fact(n-1);
  }
}
var fibonacci = function fib(n) {
  if (n <= 0) {
    return 0
  }
  if (n == 1) {
    return 1
  }
  return fib(n - 1) + fib(n - 2)
}

var gcd = function gcd(a,b){
  var counter = 1;
  var current_gcd = 0
  if (Math.max(a,b) != b) {
    gcd(b,a)
  }
  while(counter <=a){
    if(a%counter==0 && b%counter==0){
      current_gcd = counter
    }
    counter +=1
  }
  return current_gcd
}

var randS = function randomStudent(){
  var arr = ["Ahnaf", "Shafali", "Tyler", "Tom", "Matthew", "Jennifer", "Elias", "Dipali", "Sam", "Bro"]
  var randNum = Math.floor(Math.random() * arr.length)
  return arr[randNum]
  //return randNum
}
