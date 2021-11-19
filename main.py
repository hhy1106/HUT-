// ==UserScript==
// @name         湖南工业大学实验室安全考试
// @namespace    黄大帅
// @version      2.1
// @author       无敌的黄大帅
// @match        *http://172.16.50.228/redir.php?catalog_id=6&cmd=dati&moni=*
// @require      https://greasyfork.org/scripts/416691-zua-examsafety-question-bank/code/ZUA%20examsafety%20Question%20Bank.js?version=872633
// @run-at       document-end
// @grant        none
// @compatible   chrome
// @desription   我的建议是不要立马提交，做题虽然很快，但是后台如果发现你太快了会检测异常，男人不要太快了，如果不会用的话评论区叫两声。OK了
// @license      GPL-3.0-only
// ==/UserScript==

(function() {
    'use strict';
    var GridA = document.querySelector("#DataGridA > tbody");
    var timu_A = GridA.getElementsByTagName("span");
    var GridB = document.querySelector("#DataGridC > tbody");
    var timu_B = GridB.getElementsByTagName("span");
    var k = 0;

    function autoClick_answer(answer, num) {
	if (num < 8) {
		var num_index = "0".concat(num+2)
		if (answer == "A") {
			var dx_a = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(1) > label > b");
			dx_a.click();
		}
		else if (answer == "B") {
			var dx_b = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(2) > label > b");
			dx_b.click();
		}
		else if (answer == "C") {
			var dx_c = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(3) > label > b");
			dx_c.click();
		}
		else if (answer == "D") {
			var dx_d = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(4) > label > b");
			dx_d.click();
		}
		else if (answer == "正确") {
			var pd_t = document.querySelector("#DataGridC_ctl" + num_index + "_RBLCData > tbody > tr > td:nth-child(1) > label > b");
			pd_t.click();
		}
		else {
			var pd_f = document.querySelector("#DataGridC_ctl" + num_index + "_RBLCData > tbody > tr > td:nth-child(2) > label > b");
			pd_f.click();
		}
	}
	else {
		num_index = "".concat(num+2)
		if (answer == "A") {
			dx_a = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(1) > label > b");
			dx_a.click();
		}
		else if (answer == "B") {
			dx_b = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(2) > label > b");
			dx_b.click();
		}
		else if (answer == "C") {
			dx_c = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(3) > label > b");
			dx_c.click();
		}
		else if (answer == "D") {
			dx_d = document.querySelector("#DataGridA_ctl" + num_index + "_RBLAData > tbody > tr > td:nth-child(4) > label > b");
			dx_d.click();
		}
		else if (answer == "正确") {
			pd_t = document.querySelector("#DataGridC_ctl" + num_index + "_RBLCData > tbody > tr > td:nth-child(1) > label > b");
			pd_t.click();
		}
		else {
			pd_f = document.querySelector("#DataGridC_ctl" + num_index + "_RBLCData > tbody > tr > td:nth-child(2) > label > b");
			pd_f.click();
		}
	}

    }

    for (var i = 0; i < timu_A.length; i++) {
        if (timu_A[i].id.indexOf("DataGrid") != -1){
            var question_all = timu_A[i].textContent;
            var question = question_all.split(" 、")[1];
            var answer = get_answer(question);
			if (answer != "") {
				timu_A[i].innerText = timu_A[i].textContent + "==" + answer;
				autoClick_answer(answer, i);
			}
            else {
                timu_A[i].setAttribute("style", "color:red");
				k++;
            }
        }};

    for (var j = 0; j < timu_B.length; j++) {
        if (timu_B[j].id.indexOf("DataGrid") != -1){
            question_all = timu_B[j].textContent;
            question = question_all.split(" 、")[1];
            answer = get_answer(question);
			if (answer != "") {
				timu_B[j].innerText = timu_B[j].textContent + "==" + answer;
				autoClick_answer(answer, j);
			}
            else {
                timu_B[j].setAttribute("style", "color:red");
				k++;
            }
        }};
    console.log(k);
})();
