from datapackage import Package

package = Package()
package.infer(r"C:\Users\USER\Desktop\practice\city-clearance-rate\data\output.csv")
package.commit()
package.save(r"C:\Users\USER\Desktop\practice\city-clearance-rate\datapackage.json")