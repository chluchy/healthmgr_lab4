
def db_entry(df,doc):
    """ pass an existing dataframe and an instance of class specialist and update the dataframe"""
    new_data={'name':doc.name,'specialty':doc.spec,'patients':doc.pcurr,'max_patients':doc.pmax}
    df = df.append(new_data,ignore_index=True)
    return df

def doc_search(df,spec):
    """pass an existing dataframe and return any doctors who match a specified specialty"""
    doclist = []
    for i in range(len(df)):
        if df.specialty[i]==spec:
            doclist.append(df.name[i])
    if len(doclist)==0:
        return("Sorry, there are no doctors with that specialty")
    else:
        return("Doctors matching that specialty include: {}".format(', '.join(doclist)))
