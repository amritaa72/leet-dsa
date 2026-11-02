int strStr(char* haystack, char* needle) 
{
    char *match = strstr(haystack,needle);
    if (match !=NULL)
    {return match-haystack;}

    return -1;
}
