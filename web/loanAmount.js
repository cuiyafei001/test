function GetPaymentScheduleList(loanAmount, loanRate, cycle, cycleUnit){
	var multiCycles=[3,6];//多期支持的期数
	var singleCycles=[1,7,14,21,30];//单期支持的天数
	var expData=[];//期望返回值

	if (cycleUnit === 3) {
		if(multiCycles.indexOf(cycle) === -1) {
			console.log("invalid cycle");
			return expData;
		}
		var principalAndInterest0=[loanAmount*loanRate*Math.pow((1+loanRate),cycle)]/[Math.pow((1+loanRate),cycle)-1];//按公式计算出的原始每月应还本息和

		console.log("====================principalAndInterest0================"+principalAndInterest0);
		var principalAndInterest=parseInt(principalAndInterest0);//每月应还本息和（丢弃分后面的部分得到的值）
		console.log("====================principalAndInterest================"+principalAndInterest);
		var balance=Math.ceil([principalAndInterest0-Math.floor(principalAndInterest0 * 100)/100]*cycle);//首月补差
		console.log("=============Math.round(principalAndInterest0)==============="+Math.round(principalAndInterest0));
		console.log("===========principalAndInterest0-Math.round(princ	ipalAndInterest0)=============="+(principalAndInterest0-Math.round(principalAndInterest0)));
		var balance=Math.round([principalAndInterest0-Math.floor(principalAndInterest0)]*cycle);//首月补差
		console.log("=======balance========"+balance);
		var payedPrincipal = 0;
		for(var loop = 0; loop < cycle; loop++) {
			var cycleRsl = {};
			var cyclePrincipal = 0;
			var cycleInterest = 0;
			var cyclePrincipalAndInterest = 0;
			cycleInterest = Math.round((loanAmount - payedPrincipal)*loanRate);
			cyclePrincipalAndInterest = principalAndInterest;
			if (loop === 0) {
				cyclePrincipalAndInterest = principalAndInterest + balance;
			}
			cyclePrincipal = cyclePrincipalAndInterest - cycleInterest;
			payedPrincipal += cyclePrincipal;
			cycleRsl["cycleNo"] = loop + 1;
			cycleRsl["scheduleDate"]="";
			cycleRsl["principalAndInterest"]=cyclePrincipalAndInterest;
			cycleRsl["interest"]=cycleInterest;
			cycleRsl["principal"]=cyclePrincipal;
			expData[loop] = cycleRsl;
		}
		return expData;
	}
	if (cycleUnit === 1) {
		if(singleCycles.indexOf(cycle) === -1) {
			console.log("invalid cycle");
			return expData;
		}
		var cycleRsl = {};
		cycleRsl["cycleNo"] = 1;
		cycleRsl["scheduleDate"] = "";
		cycleRsl["principal"] = loanAmount;
		cycleRsl["interest"] = Math.round(loanAmount * loanRate * cycle);
		cycleRsl["principalAndInterest"] = cycleRsl["principal"] + cycleRsl["interest"];
		expData[0] = cycleRsl;

		var model=[loanAmount*loanRate*Math.pow((1+loanRate),cycle)]%[Math.pow((1+loanRate),cycle)-1];
		console.log("==============="+model);
		return expData;
	}
	return expData;
}


var loanAmount=50000;
var loanRate=0.02;
var cycle=3;
var cycleUnit=3;
var expData=GetPaymentScheduleList(loanAmount, loanRate, cycle, cycleUnit);
console.log("=========="+expData[0].cycleNo);
for(var i=0; i<expData.length; i++){
	console.log("1111===================="+expData[i].cycleNo);
	//console.log("1111===================="+expData[i].scheduleDate);
	console.log("1111===================="+expData[i].principalAndInterest);
	console.log("1111===================="+expData[i].principal);
	console.log("1111===================="+expData[i].interest);
	console.log("1111====================");
}