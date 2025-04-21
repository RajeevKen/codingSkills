package Scripts.eccap;

public class classone 
{
    /*
     * checking getter and setter example
     */
    // customer class
    private String description;
    private double prise;
    private String size = "M";
    private final double MIN_PRISE = 10.0;
    private final double MIN_TAX = 2;
    private classtwo[] items;

    public void addItems(classtwo[] someItems)
    {
        items = someItems;
    }

    public classtwo[] getItems()
    {
        return items;
    }

    public String getDiscription()
    {
        return description;
    }
    public void setDescription(String description)
    {
        this.description = description;
    }
    public double getPrise()
    {
        return prise * (1 + MIN_TAX);
    }
    public void setPrise(double prise)
    {
        this.prise = (prise > MIN_PRISE) ? prise:MIN_PRISE;
    }
    public String getSize()
    {
        return size;
    }
    public void setSize(String size)
    {
        this.size = size;
    }

}
