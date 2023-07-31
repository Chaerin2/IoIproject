// 검색 버튼 눌렀을 때 
function searchSite() {
    const searchInput = document.querySelector('input[type="text"]');
    const searchTerm = searchInput.value.trim(); //공백제거 
  
    if (searchTerm !== '') {
      // 검색어가 비어있지 않으면, 해당 검색어로 검색하는 로직 추가
      alert('"' + searchTerm + '"로 검색합니다.');
    } else {
      alert('검색어를 입력해주세요.');
    }
  }

// 버튼 클릭시 색상 바뀌게 
function changeColor(buttonId) {
    var button = document.getElementById(buttonId);
  
    // 버튼의 현재 배경색 확인
    var currentColor = window.getComputedStyle(button).backgroundColor;
  
    // 배경색이 빨간색인 경우, 기본 색상으로 변경
    if (currentColor === 'rgb(244, 67, 54)' || currentColor === '#f44336') {
      button.style.backgroundColor = ''; // 기본 색상으로 변경 (비워두면 기본 색상으로 돌아감)
    } else {
      button.style.backgroundColor = '#f44336'; // 빨간색으로 변경
    }
  }
  