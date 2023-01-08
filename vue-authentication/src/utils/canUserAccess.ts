export  const canUserAccess = async () => {
  if(localStorage.getItem('accesstoken')){
    return true;
  }
  return false;
}